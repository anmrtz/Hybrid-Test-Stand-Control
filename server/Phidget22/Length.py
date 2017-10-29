import sys
import ctypes
class Length:
	# Unknown - the default value
	IR_LENGTH_UNKNOWN = 1
	# Constant - the bitstream and gap length is constant
	IR_LENGTH_CONSTANT = 2
	# Variable - the bitstream has a variable length with a constant gap
	IR_LENGTH_VARIABLE = 3

	@classmethod
	def getName(self, val):
		if val == self.IR_LENGTH_UNKNOWN:
			return "IR_LENGTH_UNKNOWN"
		if val == self.IR_LENGTH_CONSTANT:
			return "IR_LENGTH_CONSTANT"
		if val == self.IR_LENGTH_VARIABLE:
			return "IR_LENGTH_VARIABLE"
		return "<invalid enumeration value>"
