import sys
import ctypes
class VoltageRange:
	# Range ±10mV DC
	VOLTAGE_RANGE_10mV = 1
	# Range ±40mV DC
	VOLTAGE_RANGE_40mV = 2
	# Range ±200mV DC
	VOLTAGE_RANGE_200mV = 3
	# Range ±312.5mV DC
	VOLTAGE_RANGE_312_5mV = 4
	# Range ±400mV DC
	VOLTAGE_RANGE_400mV = 5
	# Range ±1000mV DC
	VOLTAGE_RANGE_1000mV = 6
	# Range ±2V DC
	VOLTAGE_RANGE_2V = 7
	# Range ±5V DC
	VOLTAGE_RANGE_5V = 8
	# Range ±15V DC
	VOLTAGE_RANGE_15V = 9
	# Range ±40V DC
	VOLTAGE_RANGE_40V = 10
	# Auto-range mode changes based on the present voltage measurements.
	VOLTAGE_RANGE_AUTO = 11

	@classmethod
	def getName(self, val):
		if val == self.VOLTAGE_RANGE_10mV:
			return "VOLTAGE_RANGE_10mV"
		if val == self.VOLTAGE_RANGE_40mV:
			return "VOLTAGE_RANGE_40mV"
		if val == self.VOLTAGE_RANGE_200mV:
			return "VOLTAGE_RANGE_200mV"
		if val == self.VOLTAGE_RANGE_312_5mV:
			return "VOLTAGE_RANGE_312_5mV"
		if val == self.VOLTAGE_RANGE_400mV:
			return "VOLTAGE_RANGE_400mV"
		if val == self.VOLTAGE_RANGE_1000mV:
			return "VOLTAGE_RANGE_1000mV"
		if val == self.VOLTAGE_RANGE_2V:
			return "VOLTAGE_RANGE_2V"
		if val == self.VOLTAGE_RANGE_5V:
			return "VOLTAGE_RANGE_5V"
		if val == self.VOLTAGE_RANGE_15V:
			return "VOLTAGE_RANGE_15V"
		if val == self.VOLTAGE_RANGE_40V:
			return "VOLTAGE_RANGE_40V"
		if val == self.VOLTAGE_RANGE_AUTO:
			return "VOLTAGE_RANGE_AUTO"
		return "<invalid enumeration value>"
