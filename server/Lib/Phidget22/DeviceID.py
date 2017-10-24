import sys
import ctypes
class DeviceID:
	# Unknown device
	PHIDID_NOTHING = 0
	# PhidgetInterfaceKit 4/8/8
	PHIDID_INTERFACEKIT_4_8_8 = 1
	# PhidgetServo 1-Motor (1000)
	PHIDID_1000 = 2
	# PhidgetServo 4-Motor (1001)
	PHIDID_1001 = 3
	# PhidgetAnalog 4-Output (1002)
	PHIDID_1002 = 4
	# PhidgetAccelerometer 2-Axis (1008)
	PHIDID_1008 = 5
	# PhidgetInterfaceKit 8/8/8 (1010, 1013, 1018, 1019)
	PHIDID_1010_1013_1018_1019 = 6
	# PhidgetInterfaceKit 2/2/2 (1011)
	PHIDID_1011 = 7
	# PhidgetInterfaceKit 0/16/16 (1012)
	PHIDID_1012 = 8
	# PhidgetInterfaceKit 0/0/4 (1014)
	PHIDID_1014 = 9
	# PhidgetLinearTouch (1015)
	PHIDID_1015 = 10
	# PhidgetCircularTouch (1016)
	PHIDID_1016 = 11
	# PhidgetInterfaceKit 0/0/8 (1017)
	PHIDID_1017 = 12
	# PhidgetRFID (1023)
	PHIDID_1023 = 13
	# PhidgetRFID Read-Write (1024)
	PHIDID_1024 = 14
	# PhidgetLED-64 (1030)
	PHIDID_1030 = 15
	# PhidgetLED-64 Advanced (1031)
	PHIDID_1031 = 16
	# PhidgetLED-64 Advanced (1032)
	PHIDID_1032 = 17
	# PhidgetGPS (1040)
	PHIDID_1040 = 18
	# PhidgetSpatial 0/0/3 Basic (1041)
	PHIDID_1041 = 19
	# PhidgetSpatial 3/3/3 Basic (1042)
	PHIDID_1042 = 20
	# PhidgetSpatial Precision 0/0/3 High Resolution (1043)
	PHIDID_1043 = 21
	# PhidgetSpatial Precision 3/3/3 High Resolution (1044)
	PHIDID_1044 = 22
	# PhidgetTemperatureSensor IR (1045)
	PHIDID_1045 = 23
	# PhidgetBridge 4-Input (1046)
	PHIDID_1046 = 24
	# PhidgetEncoder HighSpeed 4-Input (1047)
	PHIDID_1047 = 25
	# PhidgetTemperatureSensor 4-input (1048)
	PHIDID_1048 = 26
	# PhidgetSpatial 0/0/3 (1049)
	PHIDID_1049 = 27
	# PhidgetTemperatureSensor 1-Input (1051)
	PHIDID_1051 = 28
	# PhidgetEncoder Mechanical (1052)
	PHIDID_1052 = 29
	# PhidgetAccelerometer 2-Axis (1053)
	PHIDID_1053 = 30
	# PhidgetFrequencyCounter (1054)
	PHIDID_1054 = 31
	# PhidgetIR (1055)
	PHIDID_1055 = 32
	# PhidgetSpatial 3/3/3 (1056)
	PHIDID_1056 = 33
	# PhidgetEncoder HighSpeed (1057)
	PHIDID_1057 = 34
	# PhidgetPHSensor (1058)
	PHIDID_1058 = 35
	# PhidgetAccelerometer 3-Axis (1059)
	PHIDID_1059 = 36
	# PhidgetMotorControl LV (1060)
	PHIDID_1060 = 37
	# PhidgetAdvancedServo 8-Motor (1061)
	PHIDID_1061 = 38
	# PhidgetStepper Unipolar 4-Motor (1062)
	PHIDID_1062 = 39
	# PhidgetStepper Bipolar 1-Motor (1063)
	PHIDID_1063 = 40
	# PhidgetMotorControl HC (1064)
	PHIDID_1064 = 41
	# PhidgetMotorControl 1-Motor (1065)
	PHIDID_1065 = 42
	# PhidgetAdvancedServo 1-Motor (1066)
	PHIDID_1066 = 43
	# PhidgetStepper Bipolar HC (1067)
	PHIDID_1067 = 44
	# PhidgetTextLCD 20x2 with PhidgetInterfaceKit 8/8/8 (1201, 1202, 1203)
	PHIDID_1202_1203 = 45
	# PhidgetTextLCD Adapter (1204)
	PHIDID_1204 = 46
	# PhidgetTextLCD 20x2 (1215/1216/1217/1218)
	PHIDID_1215__1218 = 47
	# PhidgetTextLCD 20x2 with PhidgetInterfaceKit 0/8/8 (1219, 1220, 1221, 1222)
	PHIDID_1219__1222 = 48
	# pH Adapter
	PHIDID_ADP1000 = 49
	# SPI Customer Interface
	PHIDID_ADP1001 = 50
	# Analog Input Module x8
	PHIDID_DAQ1000 = 51
	# Digital Input 4
	PHIDID_DAQ1200 = 52
	# Digital Input 4 Isolated
	PHIDID_DAQ1300 = 53
	# Digital Input 16
	PHIDID_DAQ1301 = 54
	# Versatile Input
	PHIDID_DAQ1400 = 55
	# Bridge
	PHIDID_DAQ1500 = 56
	# DC Motor Controller with PID
	PHIDID_DCC1000 = 57
	# 200mm Distance Sensor
	PHIDID_DST1000 = 58
	# Sonar Distance Sensor
	PHIDID_DST1200 = 59
	# Encoder
	PHIDID_ENC1000 = 60
	# Capacitive Touch Sensor
	PHIDID_HIN1000 = 61
	# Capacitive Scroll
	PHIDID_HIN1001 = 62
	# Joystick
	PHIDID_HIN1100 = 63
	# Phidget Hub with 6 ports
	PHIDID_HUB0000 = 64
	# Phidget Mesh Hub with 4 ports
	PHIDID_HUB0001 = 65
	# Phidget Mesh Dongle
	PHIDID_HUB0002 = 66
	# Phidget SPI VINT Hub with 6 ports
	PHIDID_HUB0004 = 67
	# Phidget Lightning Hub with 6 ports
	PHIDID_HUB0005 = 68
	# Humidity Sensor
	PHIDID_HUM1000 = 69
	# LCD
	PHIDID_LCD1100 = 70
	# LED Driver 32
	PHIDID_LED1000 = 71
	# Light Sensor
	PHIDID_LUX1000 = 72
	# Accelerometer 0/0/3
	PHIDID_MOT1100 = 73
	# Spatial 3/3/3
	PHIDID_MOT1101 = 74
	# Analog Output 0-5V
	PHIDID_OUT1000 = 75
	# Analog Output (+/-)10V
	PHIDID_OUT1001 = 76
	# Analog Output (+/-)10V - 16 bit
	PHIDID_OUT1002 = 77
	# Digital Output 4
	PHIDID_OUT1100 = 78
	# Barometer
	PHIDID_PRE1000 = 79
	# 8-Servo Controller
	PHIDID_RCC1000 = 80
	# Power Relay 4
	PHIDID_REL1000 = 81
	# Digital Output 4 Isolated
	PHIDID_REL1100 = 82
	# Digital Output 16 Isolated
	PHIDID_REL1101 = 83
	# Power Supply Protector
	PHIDID_SAF1000 = 84
	# Sound Pressure Level Sensor
	PHIDID_SND1000 = 85
	# Bipolar Stepper Motor Controller
	PHIDID_STC1000 = 86
	# Integrated Temperature Sensor
	PHIDID_TMP1000 = 87
	# Thermocouple 1
	PHIDID_TMP1100 = 88
	# Thermocouple 4
	PHIDID_TMP1101 = 89
	# RTD
	PHIDID_TMP1200 = 90
	# Infrared Temperature Sensor
	PHIDID_TMP1300 = 91
	# Voltage Sensor High Precision
	PHIDID_VCP1000 = 92
	# Voltage Sensor Large
	PHIDID_VCP1001 = 93
	# Voltage Sensor Small
	PHIDID_VCP1002 = 94
	# Hub Port in Digital Input mode
	PHIDID_DIGITALINPUT_PORT = 95
	# Hub Port in Digital Output mode
	PHIDID_DIGITALOUTPUT_PORT = 96
	# Hub Port in Voltage Input mode
	PHIDID_VOLTAGEINPUT_PORT = 97
	# Hub Port in Voltage Ratio Input mode
	PHIDID_VOLTAGERATIOINPUT_PORT = 98
	# Generic USB device
	PHIDID_GENERICUSB = 99
	# Generic VINT device
	PHIDID_GENERICVINT = 100
	# USB device in firmware upgrade mode
	PHIDID_FIRMWARE_UPGRADE_USB = 101
	# VINT Device in firmware upgrade mode, STM32F0 Proc.
	PHIDID_FIRMWARE_UPGRADE_STM32F0 = 102
	# VINT Device in firmware upgrade mode, STM8S Proc.
	PHIDID_FIRMWARE_UPGRADE_STM8S = 103
	# Phidget SPI device under firmware upgrade
	PHIDID_FIRMWARE_UPGRADE_SPI = 104
	# 30A Current Sensor
	PHIDID_VCP1100 = 105
	# Single Servo S2313M
	PHIDID_VINTSERVO_S2313M = 106
	# BLDC Motor Controller
	PHIDID_DCC1100 = 108
	# Dial Encoder
	PHIDID_HIN1101 = 109
	# Small DC Motor Controller
	PHIDID_DCC1001 = 110
	# Dictionary
	PHIDID_DICTIONARY = 111
	# Single Servo S3317M
	PHIDID_VINTSERVO_S3317M = 112
	# Single Servo S4309M
	PHIDID_VINTSERVO_S4309M = 113
	# Single Servo S4309R (Continuous Rotation)
	PHIDID_VINTSERVO_S4309R = 114
	# Bipolar Stepper Motor SmallController
	PHIDID_STC1001 = 115
	# OS Testing Fixture
	PHIDID_USBSWITCH = 116

	@classmethod
	def getName(self, val):
		if val == self.PHIDID_NOTHING:
			return "PHIDID_NOTHING"
		if val == self.PHIDID_INTERFACEKIT_4_8_8:
			return "PHIDID_INTERFACEKIT_4_8_8"
		if val == self.PHIDID_1000:
			return "PHIDID_1000"
		if val == self.PHIDID_1001:
			return "PHIDID_1001"
		if val == self.PHIDID_1002:
			return "PHIDID_1002"
		if val == self.PHIDID_1008:
			return "PHIDID_1008"
		if val == self.PHIDID_1010_1013_1018_1019:
			return "PHIDID_1010_1013_1018_1019"
		if val == self.PHIDID_1011:
			return "PHIDID_1011"
		if val == self.PHIDID_1012:
			return "PHIDID_1012"
		if val == self.PHIDID_1014:
			return "PHIDID_1014"
		if val == self.PHIDID_1015:
			return "PHIDID_1015"
		if val == self.PHIDID_1016:
			return "PHIDID_1016"
		if val == self.PHIDID_1017:
			return "PHIDID_1017"
		if val == self.PHIDID_1023:
			return "PHIDID_1023"
		if val == self.PHIDID_1024:
			return "PHIDID_1024"
		if val == self.PHIDID_1030:
			return "PHIDID_1030"
		if val == self.PHIDID_1031:
			return "PHIDID_1031"
		if val == self.PHIDID_1032:
			return "PHIDID_1032"
		if val == self.PHIDID_1040:
			return "PHIDID_1040"
		if val == self.PHIDID_1041:
			return "PHIDID_1041"
		if val == self.PHIDID_1042:
			return "PHIDID_1042"
		if val == self.PHIDID_1043:
			return "PHIDID_1043"
		if val == self.PHIDID_1044:
			return "PHIDID_1044"
		if val == self.PHIDID_1045:
			return "PHIDID_1045"
		if val == self.PHIDID_1046:
			return "PHIDID_1046"
		if val == self.PHIDID_1047:
			return "PHIDID_1047"
		if val == self.PHIDID_1048:
			return "PHIDID_1048"
		if val == self.PHIDID_1049:
			return "PHIDID_1049"
		if val == self.PHIDID_1051:
			return "PHIDID_1051"
		if val == self.PHIDID_1052:
			return "PHIDID_1052"
		if val == self.PHIDID_1053:
			return "PHIDID_1053"
		if val == self.PHIDID_1054:
			return "PHIDID_1054"
		if val == self.PHIDID_1055:
			return "PHIDID_1055"
		if val == self.PHIDID_1056:
			return "PHIDID_1056"
		if val == self.PHIDID_1057:
			return "PHIDID_1057"
		if val == self.PHIDID_1058:
			return "PHIDID_1058"
		if val == self.PHIDID_1059:
			return "PHIDID_1059"
		if val == self.PHIDID_1060:
			return "PHIDID_1060"
		if val == self.PHIDID_1061:
			return "PHIDID_1061"
		if val == self.PHIDID_1062:
			return "PHIDID_1062"
		if val == self.PHIDID_1063:
			return "PHIDID_1063"
		if val == self.PHIDID_1064:
			return "PHIDID_1064"
		if val == self.PHIDID_1065:
			return "PHIDID_1065"
		if val == self.PHIDID_1066:
			return "PHIDID_1066"
		if val == self.PHIDID_1067:
			return "PHIDID_1067"
		if val == self.PHIDID_1202_1203:
			return "PHIDID_1202_1203"
		if val == self.PHIDID_1204:
			return "PHIDID_1204"
		if val == self.PHIDID_1215__1218:
			return "PHIDID_1215__1218"
		if val == self.PHIDID_1219__1222:
			return "PHIDID_1219__1222"
		if val == self.PHIDID_ADP1000:
			return "PHIDID_ADP1000"
		if val == self.PHIDID_ADP1001:
			return "PHIDID_ADP1001"
		if val == self.PHIDID_DAQ1000:
			return "PHIDID_DAQ1000"
		if val == self.PHIDID_DAQ1200:
			return "PHIDID_DAQ1200"
		if val == self.PHIDID_DAQ1300:
			return "PHIDID_DAQ1300"
		if val == self.PHIDID_DAQ1301:
			return "PHIDID_DAQ1301"
		if val == self.PHIDID_DAQ1400:
			return "PHIDID_DAQ1400"
		if val == self.PHIDID_DAQ1500:
			return "PHIDID_DAQ1500"
		if val == self.PHIDID_DCC1000:
			return "PHIDID_DCC1000"
		if val == self.PHIDID_DST1000:
			return "PHIDID_DST1000"
		if val == self.PHIDID_DST1200:
			return "PHIDID_DST1200"
		if val == self.PHIDID_ENC1000:
			return "PHIDID_ENC1000"
		if val == self.PHIDID_HIN1000:
			return "PHIDID_HIN1000"
		if val == self.PHIDID_HIN1001:
			return "PHIDID_HIN1001"
		if val == self.PHIDID_HIN1100:
			return "PHIDID_HIN1100"
		if val == self.PHIDID_HUB0000:
			return "PHIDID_HUB0000"
		if val == self.PHIDID_HUB0001:
			return "PHIDID_HUB0001"
		if val == self.PHIDID_HUB0002:
			return "PHIDID_HUB0002"
		if val == self.PHIDID_HUB0004:
			return "PHIDID_HUB0004"
		if val == self.PHIDID_HUB0005:
			return "PHIDID_HUB0005"
		if val == self.PHIDID_HUM1000:
			return "PHIDID_HUM1000"
		if val == self.PHIDID_LCD1100:
			return "PHIDID_LCD1100"
		if val == self.PHIDID_LED1000:
			return "PHIDID_LED1000"
		if val == self.PHIDID_LUX1000:
			return "PHIDID_LUX1000"
		if val == self.PHIDID_MOT1100:
			return "PHIDID_MOT1100"
		if val == self.PHIDID_MOT1101:
			return "PHIDID_MOT1101"
		if val == self.PHIDID_OUT1000:
			return "PHIDID_OUT1000"
		if val == self.PHIDID_OUT1001:
			return "PHIDID_OUT1001"
		if val == self.PHIDID_OUT1002:
			return "PHIDID_OUT1002"
		if val == self.PHIDID_OUT1100:
			return "PHIDID_OUT1100"
		if val == self.PHIDID_PRE1000:
			return "PHIDID_PRE1000"
		if val == self.PHIDID_RCC1000:
			return "PHIDID_RCC1000"
		if val == self.PHIDID_REL1000:
			return "PHIDID_REL1000"
		if val == self.PHIDID_REL1100:
			return "PHIDID_REL1100"
		if val == self.PHIDID_REL1101:
			return "PHIDID_REL1101"
		if val == self.PHIDID_SAF1000:
			return "PHIDID_SAF1000"
		if val == self.PHIDID_SND1000:
			return "PHIDID_SND1000"
		if val == self.PHIDID_STC1000:
			return "PHIDID_STC1000"
		if val == self.PHIDID_TMP1000:
			return "PHIDID_TMP1000"
		if val == self.PHIDID_TMP1100:
			return "PHIDID_TMP1100"
		if val == self.PHIDID_TMP1101:
			return "PHIDID_TMP1101"
		if val == self.PHIDID_TMP1200:
			return "PHIDID_TMP1200"
		if val == self.PHIDID_TMP1300:
			return "PHIDID_TMP1300"
		if val == self.PHIDID_VCP1000:
			return "PHIDID_VCP1000"
		if val == self.PHIDID_VCP1001:
			return "PHIDID_VCP1001"
		if val == self.PHIDID_VCP1002:
			return "PHIDID_VCP1002"
		if val == self.PHIDID_DIGITALINPUT_PORT:
			return "PHIDID_DIGITALINPUT_PORT"
		if val == self.PHIDID_DIGITALOUTPUT_PORT:
			return "PHIDID_DIGITALOUTPUT_PORT"
		if val == self.PHIDID_VOLTAGEINPUT_PORT:
			return "PHIDID_VOLTAGEINPUT_PORT"
		if val == self.PHIDID_VOLTAGERATIOINPUT_PORT:
			return "PHIDID_VOLTAGERATIOINPUT_PORT"
		if val == self.PHIDID_GENERICUSB:
			return "PHIDID_GENERICUSB"
		if val == self.PHIDID_GENERICVINT:
			return "PHIDID_GENERICVINT"
		if val == self.PHIDID_FIRMWARE_UPGRADE_USB:
			return "PHIDID_FIRMWARE_UPGRADE_USB"
		if val == self.PHIDID_FIRMWARE_UPGRADE_STM32F0:
			return "PHIDID_FIRMWARE_UPGRADE_STM32F0"
		if val == self.PHIDID_FIRMWARE_UPGRADE_STM8S:
			return "PHIDID_FIRMWARE_UPGRADE_STM8S"
		if val == self.PHIDID_FIRMWARE_UPGRADE_SPI:
			return "PHIDID_FIRMWARE_UPGRADE_SPI"
		if val == self.PHIDID_VCP1100:
			return "PHIDID_VCP1100"
		if val == self.PHIDID_VINTSERVO_S2313M:
			return "PHIDID_VINTSERVO_S2313M"
		if val == self.PHIDID_DCC1100:
			return "PHIDID_DCC1100"
		if val == self.PHIDID_HIN1101:
			return "PHIDID_HIN1101"
		if val == self.PHIDID_DCC1001:
			return "PHIDID_DCC1001"
		if val == self.PHIDID_DICTIONARY:
			return "PHIDID_DICTIONARY"
		if val == self.PHIDID_VINTSERVO_S3317M:
			return "PHIDID_VINTSERVO_S3317M"
		if val == self.PHIDID_VINTSERVO_S4309M:
			return "PHIDID_VINTSERVO_S4309M"
		if val == self.PHIDID_VINTSERVO_S4309R:
			return "PHIDID_VINTSERVO_S4309R"
		if val == self.PHIDID_STC1001:
			return "PHIDID_STC1001"
		if val == self.PHIDID_USBSWITCH:
			return "PHIDID_USBSWITCH"
		return "<invalid enumeration value>"
