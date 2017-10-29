import sys
import ctypes
class VoltageOutputRange:
	# ±10V DC
	VOLTAGE_OUTPUT_RANGE_10V = 1
	# 0-5V DC
	VOLTAGE_OUTPUT_RANGE_5V = 2

	@classmethod
	def getName(self, val):
		if val == self.VOLTAGE_OUTPUT_RANGE_10V:
			return "VOLTAGE_OUTPUT_RANGE_10V"
		if val == self.VOLTAGE_OUTPUT_RANGE_5V:
			return "VOLTAGE_OUTPUT_RANGE_5V"
		return "<invalid enumeration value>"
