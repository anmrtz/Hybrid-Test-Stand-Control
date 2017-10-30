import sys
import time
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
import  RPi.GPIO as GPIO

#from test import *

# unloaded maximum speed ~200

class ValveControl():

    def __init__(self,pinCloseLimit,pinOpenLimit):
        GPIO.setmode(GPIO.BCM)
        self.pinCloseLimit = pinCloseLimit
        self.pinOpenLimit = pinOpenLimit
        GPIO.setup(self.pinCloseLimit, GPIO.IN,pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.pinOpenLimit, GPIO.IN,pull_up_down=GPIO.PUD_UP)
        
        #store reference to TestMain object
        #self.testMain = testMain

        self.fullSpeed = 100
        self.slowSpeed = 300
        self.slowAngle = 20
        self.fullOpenAngle =  90
        self.fullClosedAngle = 0
        self.bufferPercentage = 5
        self.bufferSpeedPercent = 10
        self.rescale = 0.1125
        #Calcuated
        self.bufferSpeed = 0
        self.bufferAmount = 0
        print("Valve control initialized")

        self.abortSet = False

        self.ch = None

    # Setup the Stepper object, takes serial as a value to set on
    def initStepper(self, setSerialNum = 0):#, setfullSpeed, setslowSpeed, setslowAngle, setfullOpen, setbufferPercentage, setbufferSpeedPercent):
        #self.fullSpeed = setfullSpeed
        #self.slowSpeed = setslowSpeed
        #self.slowAngle = setslowAngle
        #self.fullOpen = setfullOpen
        #self.bufferPercentage = setbufferPercentage
        #self.bufferSpeedPercent = setbufferSpeedPercent
        #Buffer calculations
        #self.bufferAmount = 90*(bufferPercentage/100)
        #self.bufferSpeed = fullSpeed*(bufferSpeedPercent/100)

        self.ch = Stepper()
        try:       
            self.ch.setOnErrorHandler(self.onErrorEvent)            
            self.ch.setOnAttachHandler(self.onStepperAttached)
            self.ch.setOnDetachHandler(self.onStepperDetached)
            #self.ch.setOnPositionChangeHandler(self.onPositionChange)

            #self.ch.setDeviceSerialNumber(setSerialNum)

            #print("Waiting for the Phidget Stepper Object to be attached...")
            self.ch.openWaitForAttachment(5000)

            #print("Stepper attached! Resuming init...")
            self.ch.setRescaleFactor(self.rescale)   
            self.ch.setVelocityLimit(self.fullSpeed)  
            self.ch.setCurrentLimit(1.8)       
            
            # Use CONTROL_MODE_RUN
            self.ch.setControlMode(1)
            self.ch.setEngaged(1)
            
            #self.ch.addPositionOffset(self.ch.getPosition())
            #print("Stepper object initialized!")
        except Exception as e:
            self.terminateValveControl("Phidget Exception " + str(e.code) + " " + e.details)
            
    def closeLimitHit(self):
        return GPIO.input(self.pinCloseLimit) == 0

    def openLimitHit(self):
        return GPIO.input(self.pinOpenLimit) == 0

    def terminateValveControl(self, msg = "NO_MSG"):
        #endTest(msg)
        print(msg)
        if (self.ch is not None):
            self.ch.setVelocityLimit(0)
            self.ch.setEngaged(0)
            self.ch.close()

    # Prints current config to console
    def testMessage(self):
        print("===========================================")
        print("Library Version: %s" % self.ch.getLibraryVersion())
        print("Serial Number: %d" % self.ch.getDeviceSerialNumber())
        print("Channel: %d" % self.ch.getChannel())
        print("Channel Class: %s" % self.ch.getChannelClass())
        print("Channel Name: %s" % self.ch.getChannelName())
        print("Device ID: %d" % self.ch.getDeviceID())
        print("Device Version: %d" % self.ch.getDeviceVersion())
        print("Device Name: %s" % self.ch.getDeviceName())
        print("Device Class: %d" % self.ch.getDeviceClass())
        print("\n")

	    # Helper functions for connection testing
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
        self.ch.close()
        self.initStepper()
        self.setVelocity(self.velocitySetting)
            
    def onErrorEvent(self, e, eCode, description):
        print("Error event #%i : %s" % (eCode, description))
        self.terminateValveControl("Phidgets onError raised")

    #Prints position to the shell (used in debugging)
    def onPositionChange(self, e, position):
        #print("Position: %f" % position)
        pass

    def openValve(self):
        #currPos = self.ch.getPosition()
        if self.abortSet:
            return
        self.setVelocity(self.slowSpeed)
        #self.ch.setTargetPosition(self.fullOpenAngle)

        while not self.openLimitHit() and not self.abortSet:
            #currPos = self.ch.getPosition()
            time.sleep(0.001)
              
        self.setVelocity(0)

    def setVelocity(self, vel):
        self.velocitySetting = vel
        try:
            self.ch.setVelocityLimit(vel)
        except Exception as e:
            print(str(e))
        
    def closeValve(self):
        #currPos = self.ch.getPosition()
        
        self.setVelocity(-self.slowSpeed)
        #self.ch.setTargetPosition(self.fullClosedAngle)

        while not self.closeLimitHit():
            #currPos = self.ch.getPosition()
            time.sleep(0.001)
        
        print("Close limit reached!")    
        self.setVelocity(0)
        
    def __del__(self):
        if self.ch is not None:
            self.ch.setEngaged(0)
            self.ch.close()
        GPIO.cleanup()


# DANGER IGNORES BUFFERS, COULD DAMAGE LIMIT SWITCHES
#def closeNoBuffer():
#    ch.setVelocityLimit(fullSpeed)
#    ch.setPosition(0)

#DANGER, DISENGAGES STEPPER, WILL ALLOW TURNING BY PRESSURE FORCE
#def UnlockValve():
#    ch.setEngaged(0)
#    GPIO.cleanup()
    
#def shutdown():
#    ch.close()

#Function activated by limit swtich detected, stops motor and does the burn
#def openDetected():
#    ch.setVelocityLimit(0)
#    time.sleep(burntime)
#    closeValve(ch,fullSpeed, bufferPercentage,bufferSpeedPercent)

#moves the valve open by 1 degree more
#def degOpen(numDeg = 1):
#    print("Opening by one degree")
#    time.sleep(0.001)
#    ch.setVelocityLimit(bufferSpeed)
#    move one dgeree at buffer speed
#    if (open_detected ==0):
#        ch.setTargetPosition(ch.getPosition()+numDeg)

#close valve by one degree
#def degClose(numDeg = 1):
#    print("Closing by one degree")
#    time.sleep(0.001)
#    ch.setVelocityLimit(bufferSpeed)
#    if (closed_detected == 0):
#        ch.setTargetPosition(ch.getPosition()-numDeg)

#Function activated by closed limit switch, stops motor
#def closeDetected():
#    ch.setVelocityLimit(0)
#    time.sleep(1)
