import sys
import ctypes
class FilterType:
	# Frequency is calculated from the number of times the signal transitions from a negative voltage to a positive voltage and back again.
	FILTER_TYPE_ZERO_CROSSING = 1
	# Frequency is calculated from the number of times the signal transitions from a logic false to a logic true and back again.
	FILTER_TYPE_LOGIC_LEVEL = 2

	@classmethod
	def getName(self, val):
		if val == self.FILTER_TYPE_ZERO_CROSSING:
			return "FILTER_TYPE_ZERO_CROSSING"
		if val == self.FILTER_TYPE_LOGIC_LEVEL:
			return "FILTER_TYPE_LOGIC_LEVEL"
		return "<invalid enumeration value>"
