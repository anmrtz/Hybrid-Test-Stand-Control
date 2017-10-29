import sys
import ctypes
class VoltageSensorType:
	# Default. Configures the channel to be a generic voltage sensor. Unit is volts.
	SENSOR_TYPE_VOLTAGE = 0
	# 1114 - Temperature Sensor
	SENSOR_TYPE_1114 = 11140
	# 1117 - Voltage Sensor
	SENSOR_TYPE_1117 = 11170
	# 1123 - Precision Voltage Sensor
	SENSOR_TYPE_1123 = 11230
	# 1127 - Precision Light Sensor
	SENSOR_TYPE_1127 = 11270
	# 1130 - pH Adapter
	SENSOR_TYPE_1130_PH = 11301
	# 1130 - ORP Adapter
	SENSOR_TYPE_1130_ORP = 11302
	# 1132 - 4-20mA Adapter
	SENSOR_TYPE_1132 = 11320
	# 1133 - Sound Sensor
	SENSOR_TYPE_1133 = 11330
	# 1135 - Precision Voltage Sensor
	SENSOR_TYPE_1135 = 11350
	# 1142 - Light Sensor 1000 lux
	SENSOR_TYPE_1142 = 11420
	# 1143 - Light Sensor 70000 lux
	SENSOR_TYPE_1143 = 11430
	# 3500 - AC Current Sensor 10Amp
	SENSOR_TYPE_3500 = 35000
	# 3501 - AC Current Sensor 25Amp
	SENSOR_TYPE_3501 = 35010
	# 3502 - AC Current Sensor 50Amp
	SENSOR_TYPE_3502 = 35020
	# 3503 - AC Current Sensor 100Amp
	SENSOR_TYPE_3503 = 35030
	# 3507 - AC Voltage Sensor 0-250V (50Hz)
	SENSOR_TYPE_3507 = 35070
	# 3508 - AC Voltage Sensor 0-250V (60Hz)
	SENSOR_TYPE_3508 = 35080
	# 3509 - DC Voltage Sensor 0-200V
	SENSOR_TYPE_3509 = 35090
	# 3510 - DC Voltage Sensor 0-75V
	SENSOR_TYPE_3510 = 35100
	# 3511 - DC Current Sensor 0-10mA
	SENSOR_TYPE_3511 = 35110
	# 3512 - DC Current Sensor 0-100mA
	SENSOR_TYPE_3512 = 35120
	# 3513 - DC Current Sensor 0-1A
	SENSOR_TYPE_3513 = 35130
	# 3514 - AC Active Power Sensor 0-250V*0-30A (50Hz)
	SENSOR_TYPE_3514 = 35140
	# 3515 - AC Active Power Sensor 0-250V*0-30A (60Hz)
	SENSOR_TYPE_3515 = 35150
	# 3516 - AC Active Power Sensor 0-250V*0-5A (50Hz)
	SENSOR_TYPE_3516 = 35160
	# 3517 - AC Active Power Sensor 0-250V*0-5A (60Hz)
	SENSOR_TYPE_3517 = 35170
	# 3518 - AC Active Power Sensor 0-110V*0-5A (60Hz)
	SENSOR_TYPE_3518 = 35180
	# 3519 - AC Active Power Sensor 0-110V*0-15A (60Hz)
	SENSOR_TYPE_3519 = 35190
	# 3584 - 0-50A DC Current Transducer
	SENSOR_TYPE_3584 = 35840
	# 3585 - 0-100A DC Current Transducer
	SENSOR_TYPE_3585 = 35850
	# 3586 - 0-250A DC Current Transducer
	SENSOR_TYPE_3586 = 35860
	# 3587 - +-50A DC Current Transducer
	SENSOR_TYPE_3587 = 35870
	# 3588 - +-100A DC Current Transducer
	SENSOR_TYPE_3588 = 35880
	# 3589 - +-250A DC Current Transducer
	SENSOR_TYPE_3589 = 35890

	@classmethod
	def getName(self, val):
		if val == self.SENSOR_TYPE_VOLTAGE:
			return "SENSOR_TYPE_VOLTAGE"
		if val == self.SENSOR_TYPE_1114:
			return "SENSOR_TYPE_1114"
		if val == self.SENSOR_TYPE_1117:
			return "SENSOR_TYPE_1117"
		if val == self.SENSOR_TYPE_1123:
			return "SENSOR_TYPE_1123"
		if val == self.SENSOR_TYPE_1127:
			return "SENSOR_TYPE_1127"
		if val == self.SENSOR_TYPE_1130_PH:
			return "SENSOR_TYPE_1130_PH"
		if val == self.SENSOR_TYPE_1130_ORP:
			return "SENSOR_TYPE_1130_ORP"
		if val == self.SENSOR_TYPE_1132:
			return "SENSOR_TYPE_1132"
		if val == self.SENSOR_TYPE_1133:
			return "SENSOR_TYPE_1133"
		if val == self.SENSOR_TYPE_1135:
			return "SENSOR_TYPE_1135"
		if val == self.SENSOR_TYPE_1142:
			return "SENSOR_TYPE_1142"
		if val == self.SENSOR_TYPE_1143:
			return "SENSOR_TYPE_1143"
		if val == self.SENSOR_TYPE_3500:
			return "SENSOR_TYPE_3500"
		if val == self.SENSOR_TYPE_3501:
			return "SENSOR_TYPE_3501"
		if val == self.SENSOR_TYPE_3502:
			return "SENSOR_TYPE_3502"
		if val == self.SENSOR_TYPE_3503:
			return "SENSOR_TYPE_3503"
		if val == self.SENSOR_TYPE_3507:
			return "SENSOR_TYPE_3507"
		if val == self.SENSOR_TYPE_3508:
			return "SENSOR_TYPE_3508"
		if val == self.SENSOR_TYPE_3509:
			return "SENSOR_TYPE_3509"
		if val == self.SENSOR_TYPE_3510:
			return "SENSOR_TYPE_3510"
		if val == self.SENSOR_TYPE_3511:
			return "SENSOR_TYPE_3511"
		if val == self.SENSOR_TYPE_3512:
			return "SENSOR_TYPE_3512"
		if val == self.SENSOR_TYPE_3513:
			return "SENSOR_TYPE_3513"
		if val == self.SENSOR_TYPE_3514:
			return "SENSOR_TYPE_3514"
		if val == self.SENSOR_TYPE_3515:
			return "SENSOR_TYPE_3515"
		if val == self.SENSOR_TYPE_3516:
			return "SENSOR_TYPE_3516"
		if val == self.SENSOR_TYPE_3517:
			return "SENSOR_TYPE_3517"
		if val == self.SENSOR_TYPE_3518:
			return "SENSOR_TYPE_3518"
		if val == self.SENSOR_TYPE_3519:
			return "SENSOR_TYPE_3519"
		if val == self.SENSOR_TYPE_3584:
			return "SENSOR_TYPE_3584"
		if val == self.SENSOR_TYPE_3585:
			return "SENSOR_TYPE_3585"
		if val == self.SENSOR_TYPE_3586:
			return "SENSOR_TYPE_3586"
		if val == self.SENSOR_TYPE_3587:
			return "SENSOR_TYPE_3587"
		if val == self.SENSOR_TYPE_3588:
			return "SENSOR_TYPE_3588"
		if val == self.SENSOR_TYPE_3589:
			return "SENSOR_TYPE_3589"
		return "<invalid enumeration value>"
