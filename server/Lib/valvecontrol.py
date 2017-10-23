import sys
import time
from Phidget22.Devices.Stepper import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
# Setup the Stepper object, takes serial as a value to set on


def SetupStepper(serial):
    try:
        ch = Stepper()
        ch.setOnAttachHandler(StepperAttached)
        ch.setOnDetachHandler(StepperDetached)
        ch.setOnErrorHandler(ErrorEvent)
        ch.setOnPositionChangeHandler(PositionChangeHandler)
        #ch.setDeviceSerialNumber(serial)
        print("Waiting for the Phidget Stepper Object to be attached...")
        ch.openWaitForAttachment(5000)
        # ch.setChannel(channel)
        ch.setEngaged(1)
        return ch
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)

# Prints current config to console


def testMessage(ch):
    attached = ch
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

# Helper functions for connection testing

def StepperAttached(e):
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
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)
    
def StepperDetached(e):
    detached = e
    try:
        print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Press Enter to Exit...\n")
        readin = sys.stdin.read(1)
        exit(1)   

#Helper to print passed error messages to the shell
def ErrorEvent(e, eCode, description):
    print("Error %i : %s" % (eCode, description))

#Prints position to the shell (used in debugging)

def PositionChangeHandler(e, position):
    print("Position: %f" % position)
# Pass rescale value to allow work in degrees (in our case 0.1125)

def SetRescale(ch, value):
    ch.setRescaleFactor(value)

# Grab the current postion and set as the zero positon


def SetStart(ch):
    ch.addPositionOffset(ch.getPosition())

# Function to open valve, slowly at first, then full speed with buffers to prevent limit switch damage
# This should be interupted by limit switches


def OpenValve(ch, slowSpeed, slowAngle, fullSpeed, fullOpen, bufferPercentage,bufferSpeedPercent):
    currPos = 0
    bufferAmount = 90*(bufferPercentage/100)
    bufferSpeed = fullSpeed*(bufferSpeedPercent/100)
    bufferedAngle = fullOpen-bufferAmount
    ch.setVelocityLimit(slowSpeed)
    ch.setTargetPosition(slowAngle)
    while currPos < slowAngle:
        # do nothing until we hit angle we want
        currPos = ch.getPosition()
    ch.setVelocityLimit(fullSpeed)
    ch.setTargetPosition(fullOpen-bufferAmount)
    while currPos < bufferedAngle:
        # do nothing until we hit angle we want
        currPos = ch.getPosition()
    ch.setVelocityLimit(bufferSpeed)
    ch.setTargetPosition(fullOpen)

# Function to close valve with buffers an


def closeValve(ch,fullSpeed, bufferPercentage,bufferSpeedPercent):
    currPos = ch.getPosition()
    bufferAmount = 90*(bufferPercentage/100)
    bufferSpeed = fullSpeed*(bufferSpeedPercent/100)
    ch.setVelocityLimit(fullSpeed)
    ch.setTargetPosition(bufferAmount)
    while currPos > bufferAmount:
        # do nothing until we hit angle we want
        currPos=ch.getPosition()
    ch.setVelocityLimit(bufferSpeed)
    ch.setTargetPosition(0)
    time.sleep(1)

# DANGER IGNORES BUFFERS, COULD DAMAGE LIMIT SWITCHES


def closeNoBuffer(fullSpeed):
    ch.setVelocityLimit(fullSpeed)
    ch.setPosition(0)
    
#DANGER, DISENGAGES STEPPER, WILL ALLOW TURNING BY PRESSURE FORCE
    
def UnlockValve(ch):
    ch.setEngaged(0)
