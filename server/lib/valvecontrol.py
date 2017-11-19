import sys
import time
from Phidget22.Devices.Encoder import *
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
import  RPi.GPIO as GPIO

from testmain import testEnded
from testmain import endTest

class ValveControl():

	_MAX_SPEED = 300
	_DEFAULT_SPEED = 200
	_RESCALE_FACTOR = 0.1125

	def __init__(self, pinCloseLimit = 21, pinOpenLimit = 26, pinAlwaysClosedValve = 20, testMain = None):
		GPIO.setmode(GPIO.BCM)
		self.pinCloseLimit = pinCloseLimit
		self.pinOpenLimit = pinOpenLimit
		GPIO.setup(self.pinCloseLimit, GPIO.IN,pull_up_down=GPIO.PUD_UP)
		GPIO.setup(self.pinOpenLimit, GPIO.IN,pull_up_down=GPIO.PUD_UP)
		
		#store reference to parent TestMain object
		self.testMain = testMain

		self.velocitySetting = 0
		#self.slowAngle = 20
		self.fullOpenAngle =  90
		self.fullClosedAngle = 0
		#self.bufferPercentage = 5
		#self.bufferSpeedPercent = 10
		#self.rescale = 0.1125
		#Calcuated
		#self.bufferSpeed = 0
		#self.bufferAmount = 0
		self.burn_duration = 0 
		print("Valve control initialized")

		#self.abortSet = False

		assert ValveControl._MAX_SPEED > 0
		assert ValveControl._DEFAULT_SPEED > 0
		assert ValveControl._DEFAULT_SPEED <= ValveControl._MAX_SPEED

		self.stepper = None
		self.encoder = None
		self.motorPos = 0

	# Setup the Stepper object, takes serial as a value to set on
	def initStepper(self):#, setfullSpeed, setslowSpeed, setslowAngle, setfullOpen, setbufferPercentage, setbufferSpeedPercent):
		#self.fullSpeed = setfullSpeed
		#self.slowSpeed = setslowSpeed
		#self.slowAngle = setslowAngle
		#self.fullOpen = setfullOpen
		#self.bufferPercentage = setbufferPercentage
		#self.bufferSpeedPercent = setbufferSpeedPercent
		#Buffer calculations
		#self.bufferAmount = 90*(bufferPercentage/100)
		#self.bufferSpeed = fullSpeed*(bufferSpeedPercent/100)

		self.stepper = Stepper()
		try:       
			self.stepper.setDeviceSerialNumber(423768)
			self.stepper.setChannel(0)

			self.stepper.setOnErrorHandler(self.onErrorEvent)            
			self.stepper.setOnAttachHandler(self.onStepperAttached)
			self.stepper.setOnDetachHandler(self.onStepperDetached)

			self.stepper.openWaitForAttachment(5000)

			self.stepper.setRescaleFactor(ValveControl._RESCALE_FACTOR)   
			self.stepper.setVelocityLimit(ValveControl._MAX_SPEED)  
			self.stepper.setCurrentLimit(1.8)       
			
			# Use CONTROL_MODE_RUN
			self.stepper.setControlMode(1)
			self.stepper.setEngaged(1)
			
			#self.stepper.addPositionOffset(self.stepper.getPosition())
			#print("Stepper object initialized!")
		except Exception as e:
			self.terminateValveControl("Phidget Exception " + str(e.code) + " " + e.details)
	
	def initEncoder(self, initPosition = 0):
		self.encoder = Encoder()
		try:
			self.encoder.setDeviceSerialNumber(426800)
			self.encoder.setChannel(0)

			self.encoder.setOnAttachHandler(self.onEncoderAttached)
			self.encoder.setOnDetachHandler(self.onEncoderDetached)
			self.encoder.setOnErrorHandler(self.onErrorEvent)
	
			self.encoder.setOnPositionChangeHandler(self.onPositionChanged)

			self.encoder.openWaitForAttachment(5000)
			self.encoder.setPosition(initPosition)
			self.encoder.setDataInterval(10)
			if(not self.encoder.getEnabled()):
				self.encoder.setEnabled(1)

		except Exception as e:
			self.terminateValveControl("Exception " + str(e))
	
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
		except PhidgetException as e:
			print("Phidget Exception %i: %s" % (e.code, e.details))

	def onEncoderDetached(self, e):
		try:
			print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
		except PhidgetException as e:
			terminateValveControl("encoder detached! Phidget Exception " + str(e.code) + " " + e.details)
		try:
			tempVelocity = self.velocitySetting
			self.setVelocity(0)
			tempPosition = self.encoder.getPosition()
			self.encoder.close()
			self.initEncoder(tempPosition)
			self.setVelocity(tempVelocity)
		except Exception as e:
			terminateValveControl("failed to recover from encoder detach event! " + str(e.code) + " " + e.details)
				

	def onPositionChanged(self, e, positionChange, timeChange, indexTriggered):
		self.motorPos = self.encoder.getPosition()
		#curr_pos = ch.getPosition() 
		#print("Position Changed: %7d %7d  %7.3lf  %d\n" % (curr_pos, positionChange, timeChange, indexTriggered))	
	
	def loadSettings(self,settings):
		if len(params) != 10:
			endTest('Need 10 input parameters')
			return
		try:
			self.burn_duration = float(params[1])
			#not used yet
			#self.ignitor_timing = float(params[2])
			self.valve_open_timing = float(params[3])
			self.valve_closing_time = float(params[4])
			#self.bufferSpeedPercent = float(params[5])
			#self.bufferPercentage = float(params[6])

			#These need to be modified according to opening methods (time v speed)
		    #self.fullSpeed= float(params[7])
			#self.slowSpeed = float(params[8])
			#self.slowAngle = float(params[9])
		except:
			print("Malformed passed data!")
			return

	def closeLimitHit(self):
		return GPIO.input(self.pinCloseLimit) == 0

	def openLimitHit(self):
		return GPIO.input(self.pinOpenLimit) == 0

	def terminateValveControl(self, msg = "NO_MSG"):
		endTest(msg)
		print(msg)
		if (self.stepper is not None):
			self.stepper.setVelocityLimit(0)
			self.stepper.setEngaged(0)
			self.stepper.close()

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

	def openValve(self):
		#currPos = self.stepper.getPosition()
		if testEnded():
			return
		self.setVelocity(ValveControl._DEFAULT_SPEED)
		#self.stepper.setTargetPosition(self.fullOpenAngle)

		while not self.openLimitHit() and not testEnded():
			#currPos = self.stepper.getPosition()
			time.sleep(0.001)
			  
		self.setVelocity(0)
		#print("Finished opening!")

	def setVelocity(self, vel):
		assert abs(vel) <= ValveControl._MAX_SPEED
		self.velocitySetting = vel
		try:
			self.stepper.setVelocityLimit(vel)
		except Exception as e:
			print(str(e))
		
	def closeValve(self):
		#currPos = self.stepper.getPosition()
		
		self.setVelocity(-ValveControl._DEFAULT_SPEED)
		#self.stepper.setTargetPosition(self.fullClosedAngle)

		while not self.closeLimitHit():
			#currPos = self.stepper.getPosition()
			time.sleep(0.001)
			
		self.setVelocity(0)
		#print("Finished closing!")
		
	def __del__(self):
		if self.stepper is not None:
			self.stepper.setEngaged(0)
			self.stepper.close()

		if self.encoder is not None:
			self.encoder.close()

		GPIO.cleanup()

