import sys
import time
from Phidget22.Devices.Encoder import *
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
import RPi.GPIO as GPIO

from testmain import testEnded
from testmain import endTest

#Set this flag to true when the vent stepper motor + Phidgets board are available
_VENT_VALVE_ENABLED = True

class StepperController():

	def __init__(self, serialNum, rescaleFactor, defaultVel, maxVelocity = 360, currentLimit = 1.8):
		self.stepper = None
		self.serialNum = serialNum
		self.defaultVelocity = defaultVel
		self.maxVelocity = maxVelocity
		self.rescaleFactor = rescaleFactor
		self.currentLimit = currentLimit
		self.velocitySetting = 0
		
		self.initStepper()
		
	def initStepper(self):
		self.stepper = Stepper()
		try:       
			self.stepper.setDeviceSerialNumber(self.serialNum)
			self.stepper.setChannel(0)

			self.stepper.setOnErrorHandler(self.onErrorEvent)            
			self.stepper.setOnAttachHandler(self.onStepperAttached)
			self.stepper.setOnDetachHandler(self.onStepperDetached)

			self.stepper.openWaitForAttachment(5000)

			self.stepper.setRescaleFactor(self.rescaleFactor)   
			self.stepper.setVelocityLimit(self.maxVelocity)  
			self.stepper.setCurrentLimit(self.currentLimit)       
			
			# Use CONTROL_MODE_RUN
			self.stepper.setControlMode(1)
			self.stepper.setEngaged(1)

		except PhidgetException as e:
			self.terminateValveControl("Phidget Exception " + str(e.code) + " " + e.details)

	def onStepperAttached(self,attached):
		try:
			print("\nAttach Event Detected (Information Below)")
			print("===========================================")
			print("Library Version: %s" % attached.getLibraryVersion())
			print("Serial Number: %d" % attached.getDeviceSerialNumber())
			print("Channel: %d" % attached.getChannel())
			print("Channel Class: %s" % attached.getChannelClass())
			print("Channel Name: %s" % attached.getChannelName())
			print("Device ID: %d" % attached.getDeviceID())
			print("Device Version: %d" % attached.getDeviceVersion())
			print("Device Name: %s" % attached.getDeviceName())
			print("Device Class: %d" % attached.getDeviceClass())
			print("\n")

		except PhidgetException as e:
			self.terminateValveControl("Phidget Exception " + str(e.code) + " " + e.details)
		
	def onStepperDetached(self, detached):
		try:
			print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
		except PhidgetException as e:
			terminateValveControl("onStepperDetached! Phidget Exception " + str(e.code) + " " + e.details)
		self.stepper.close()
		self.initStepper()
		self.setVelocity(self.velocitySetting)

	def onErrorEvent(self, e, eCode, description):
		print("Error event #%i : %s" % (eCode, description))
		self.terminateValveControl("Phidgets onError raised")			

	def terminateValveControl(self, msg = "NO_MSG"):
		endTest(msg)
		print(msg)
		if (self.stepper is not None):
			self.stepper.setVelocityLimit(0)
			self.stepper.setEngaged(0)
			self.stepper.close()

	def setVelocity(self, vel):
		assert abs(vel) <= self.maxVelocity
		self.velocitySetting = vel
		try:
			self.stepper.setVelocityLimit(vel)
		except Exception as e:
			print(str(e))

	def setDefaultVelocity(self, newDefaultVel):
		if (newDefaultVel > 0 and newDefaultVel <= self.maxVelocity):
			self.defaultVelocity = newDefaultVel
			return "Default velocity set to " + str(newDefaultVel) + " deg/s"
		else:
			return "Set default velocity error: value out of range"

	def __del__(self):
		if (self.stepper is not None):
			try:
				self.setVelocity(0)
				self.stepper.setEngaged(0)
			except Exception:
				print("Failed to deactive stepper")

class ValveControl():

	_ENCODER_COUNT_PER_DEGREES = 300.0 / 90.0
	_DEGREES_PER_ENCODER_COUNT = 90.0 / 300.0

	def __init__(self, MEVStepperSerialNum = 423768, ventStepperSerialNum = 507392, encoderSerialNum = 426800, pinMEVCloseLimit = 5, pinMEVOpenLimit = 6, pinNCValve = 20, pinIgnitor = 16, pinNCValveRelayIn = 12, pinIgnitorRelayIn = 26, pinLockoutIn = 13, pinVentCloseLimit = 25, pinVentOpenLimit = 21):
		GPIO.setmode(GPIO.BCM)

		self.pinMEVCloseLimit = pinMEVCloseLimit
		GPIO.setup(self.pinMEVCloseLimit, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		self.pinMEVOpenLimit = pinMEVOpenLimit
		GPIO.setup(self.pinMEVOpenLimit, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		self.pinVentCloseLimit = pinVentCloseLimit
		GPIO.setup(self.pinVentCloseLimit, GPIO.IN, pull_up_down=GPIO.PUD_UP)

		self.pinVentOpenLimit = pinVentOpenLimit
		GPIO.setup(self.pinVentOpenLimit, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		
		self.pinIgnitor = pinIgnitor
		GPIO.setup(self.pinIgnitor, GPIO.OUT)
		
		self.pinNCValve = pinNCValve
		GPIO.setup(self.pinNCValve, GPIO.OUT)

		self.pinIgnitorRelayIn = pinIgnitorRelayIn
		GPIO.setup(self.pinIgnitorRelayIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		

		self.pinNCValveRelayIn = pinNCValveRelayIn
		GPIO.setup(self.pinNCValveRelayIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		
		
		self.pinLockoutIn = pinLockoutIn
		GPIO.setup(self.pinLockoutIn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)		

		self.fullOpenAngle =  90
		self.fullClosedAngle = 0
		self.burn_duration = 0 

		self.MEVStepper = StepperController(MEVStepperSerialNum, 0.1125, 180, 360)
		self.ventStepper = None
		if _VENT_VALVE_ENABLED:
			self.ventStepper = StepperController(ventStepperSerialNum, 0.0021875, 45, 90)

		self.initEncoder(encoderSerialNum)
		self.motorPos = 0
			
	def initEncoder(self, serialNum, initPosition = 0):
		self.encoder = Encoder()
		try:
			self.encoder.setDeviceSerialNumber(serialNum)
			self.encoder.setChannel(0)

			self.encoder.setOnAttachHandler(self.onEncoderAttached)
			self.encoder.setOnDetachHandler(self.onEncoderDetached)
			self.encoder.setOnErrorHandler(self.onErrorEvent)
	
			#self.encoder.setOnPositionChangeHandler(self.onPositionChanged)

			self.encoder.openWaitForAttachment(5000)
			self.encoder.setPosition(initPosition)
			self.encoder.setDataInterval(10)
			if(not self.encoder.getEnabled()):
				self.encoder.setEnabled(1)
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))
			endTest("Encoder init error")

		#except Exception as e:
		#	self.MEVStepper.terminateValveControl("init encoder error")
		#	self.ventStepper.terminateValveControl("init encoder error")
	
	def onEncoderAttached(self, e):
		try:
			attached = e
			print("\nAttach Event Detected (Information Below)")
			print("===========================================")
			print("Library Version: %s" % attached.getLibraryVersion())
			print("Serial Number: %d" % attached.getDeviceSerialNumber())
			print("Channel: %d" % attached.getChannel())
			print("Channel Class: %s" % attached.getChannelClass())
			print("Channel Name: %s" % attached.getChannelName())
			print("Device ID: %d" % attached.getDeviceID())
			print("Device Version: %d" % attached.getDeviceVersion())
			print("Device Name: %s" % attached.getDeviceName())
			print("Device Class: %d" % attached.getDeviceClass())
			print("\n")
		except Exception as e:
			endTest("Encoder attached error")

	def onEncoderDetached(self, e):
		try:
			print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
		except PhidgetException as e:
			terminateValveControl("encoder detached! Phidget Exception " + str(e.code) + " " + e.details)
		try:
			tempVelocity = self.velocitySetting
			self.MEVStepper.setVelocity(0)
			tempPosition = self.encoder.getPosition()
			self.encoder.close()
			self.initEncoder(tempPosition)
			self.MEVStepper.setVelocity(tempVelocity)
		except Exception as e:
			endTest("Encoder detached error")

	def onErrorEvent(self, e, eCode, description):
		print("Error event #%i : %s" % (eCode, description))
		endTest("Encoder error")
						
	def calibratePosition(self, position = 0):
		self.encoder.setPosition(position)
		
	def MEVCloseLimitHit(self):
		return GPIO.input(self.pinMEVCloseLimit) == 0

	def MEVOpenLimitHit(self):
		return GPIO.input(self.pinMEVOpenLimit) == 0

	def VentCloseLimitHit(self):
		return GPIO.input(self.pinVentCloseLimit) == 0

	def VentOpenLimitHit(self):
		return GPIO.input(self.pinVentOpenLimit) == 0
			
	def moveMEVByAngle(self, angleDegrees, velocity):
		encoderTarget = self.encoder.getPosition() + (angleDegrees * ValveControl._ENCODER_COUNT_PER_DEGREES)
		#towards closed position
		if (angleDegrees < 0):
			self.MEVStepper.setVelocity(-velocity)
			while self.encoder.getPosition() > encoderTarget and not self.MEVCloseLimitHit() and not testEnded():
				time.sleep(0.001)
		#towards open position
		elif (angleDegrees > 0):
			self.MEVStepper.setVelocity(velocity)
			while self.encoder.getPosition() < encoderTarget and not self.MEVOpenLimitHit() and not testEnded():
				time.sleep(0.001)
		self.MEVStepper.setVelocity(0)
		
	def moveMEVToAngle(self, targetAngleDegrees, velocity):
		travelDistance = targetAngleDegrees - (self.encoder.getPosition() *  ValveControl._DEGREES_PER_ENCODER_COUNT)
		self.moveMEVByAngle(travelDistance, velocity)

	def moveMEVToOpenLimit(self):
		if testEnded():
			return
		self.MEVStepper.setVelocity(self.MEVStepper.defaultVelocity)
		while not self.MEVOpenLimitHit() and not testEnded():
			time.sleep(0.001)			  
		self.MEVStepper.setVelocity(0)
		
	def moveMEVToCloseLimit(self):
		self.MEVStepper.setVelocity(-self.MEVStepper.defaultVelocity)
		while not self.MEVCloseLimitHit():
			time.sleep(0.001)			
		self.MEVStepper.setVelocity(0)

	def moveVentToOpenLimit(self):
		if self.ventStepper is None:
			return

		if testEnded():
			return
		self.ventStepper.setVelocity(-self.ventStepper.defaultVelocity)
		while not self.VentOpenLimitHit() and not testEnded():
			time.sleep(0.001)			  
		self.ventStepper.setVelocity(0)
		
	def moveVentToCloseLimit(self):
		if self.ventStepper is None:
			return

		self.ventStepper.setVelocity(self.ventStepper.defaultVelocity)
		while not self.VentCloseLimitHit():
			time.sleep(0.001)			
		self.ventStepper.setVelocity(0)

	def setIgnitor(self, active):
		GPIO.output(self.pinIgnitor, active)
		
	def setNCValve(self, active):
		GPIO.output(self.pinNCValve, active)
			
	def ignitorActive(self):
		return GPIO.input(self.pinIgnitorRelayIn) != 0

	def NCValveActive(self):
		return GPIO.input(self.pinNCValveRelayIn) != 0
		
	def lockoutArmed(self):
		return GPIO.input(self.pinLockoutIn) != 0
		
	def __del__(self):
		GPIO.cleanup()

