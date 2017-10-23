import sys
import ctypes
class DeviceClass:
	# Any device
	PHIDCLASS_NOTHING = 0
	# PhidgetAccelerometer device
	PHIDCLASS_ACCELEROMETER = 1
	# PhidgetAdvancedServo device
	PHIDCLASS_ADVANCEDSERVO = 2
	# PhidgetAnalog device
	PHIDCLASS_ANALOG = 3
	# PhidgetBridge device
	PHIDCLASS_BRIDGE = 4
	# PhidgetEncoder device
	PHIDCLASS_ENCODER = 5
	# PhidgetFrequencyCounter device
	PHIDCLASS_FREQUENCYCOUNTER = 6
	# PhidgetGPS device
	PHIDCLASS_GPS = 7
	# Phidget VINT Hub device
	PHIDCLASS_HUB = 8
	# PhidgetInterfaceKit device
	PHIDCLASS_INTERFACEKIT = 9
	# PhidgetIR device
	PHIDCLASS_IR = 10
	# PhidgetLED device
	PHIDCLASS_LED = 11
	# Phidget Mesh Dongle
	PHIDCLASS_MESHDONGLE = 12
	# PhidgetMotorControl device
	PHIDCLASS_MOTORCONTROL = 13
	# PhidgetPHSensor device
	PHIDCLASS_PHSENSOR = 14
	# PhidgetRFID device
	PHIDCLASS_RFID = 15
	# PhidgetServo device
	PHIDCLASS_SERVO = 16
	# PhidgetSpatial device
	PHIDCLASS_SPATIAL = 17
	# PhidgetStepper device
	PHIDCLASS_STEPPER = 18
	# PhidgetTemperatureSensor device
	PHIDCLASS_TEMPERATURESENSOR = 19
	# PhidgetTextLCD device
	PHIDCLASS_TEXTLCD = 20
	# Phidget VINT device
	PHIDCLASS_VINT = 21
	# Generic device
	PHIDCLASS_GENERIC = 22
	# Phidget device in Firmware Upgrade mode
	PHIDCLASS_FIRMWAREUPGRADE = 23
	# Dictionary device
	PHIDCLASS_DICTIONARY = 24

	@classmethod
	def getName(self, val):
		if val == self.PHIDCLASS_NOTHING:
			return "PHIDCLASS_NOTHING"
		if val == self.PHIDCLASS_ACCELEROMETER:
			return "PHIDCLASS_ACCELEROMETER"
		if val == self.PHIDCLASS_ADVANCEDSERVO:
			return "PHIDCLASS_ADVANCEDSERVO"
		if val == self.PHIDCLASS_ANALOG:
			return "PHIDCLASS_ANALOG"
		if val == self.PHIDCLASS_BRIDGE:
			return "PHIDCLASS_BRIDGE"
		if val == self.PHIDCLASS_ENCODER:
			return "PHIDCLASS_ENCODER"
		if val == self.PHIDCLASS_FREQUENCYCOUNTER:
			return "PHIDCLASS_FREQUENCYCOUNTER"
		if val == self.PHIDCLASS_GPS:
			return "PHIDCLASS_GPS"
		if val == self.PHIDCLASS_HUB:
			return "PHIDCLASS_HUB"
		if val == self.PHIDCLASS_INTERFACEKIT:
			return "PHIDCLASS_INTERFACEKIT"
		if val == self.PHIDCLASS_IR:
			return "PHIDCLASS_IR"
		if val == self.PHIDCLASS_LED:
			return "PHIDCLASS_LED"
		if val == self.PHIDCLASS_MESHDONGLE:
			return "PHIDCLASS_MESHDONGLE"
		if val == self.PHIDCLASS_MOTORCONTROL:
			return "PHIDCLASS_MOTORCONTROL"
		if val == self.PHIDCLASS_PHSENSOR:
			return "PHIDCLASS_PHSENSOR"
		if val == self.PHIDCLASS_RFID:
			return "PHIDCLASS_RFID"
		if val == self.PHIDCLASS_SERVO:
			return "PHIDCLASS_SERVO"
		if val == self.PHIDCLASS_SPATIAL:
			return "PHIDCLASS_SPATIAL"
		if val == self.PHIDCLASS_STEPPER:
			return "PHIDCLASS_STEPPER"
		if val == self.PHIDCLASS_TEMPERATURESENSOR:
			return "PHIDCLASS_TEMPERATURESENSOR"
		if val == self.PHIDCLASS_TEXTLCD:
			return "PHIDCLASS_TEXTLCD"
		if val == self.PHIDCLASS_VINT:
			return "PHIDCLASS_VINT"
		if val == self.PHIDCLASS_GENERIC:
			return "PHIDCLASS_GENERIC"
		if val == self.PHIDCLASS_FIRMWAREUPGRADE:
			return "PHIDCLASS_FIRMWAREUPGRADE"
		if val == self.PHIDCLASS_DICTIONARY:
			return "PHIDCLASS_DICTIONARY"
		return "<invalid enumeration value>"
