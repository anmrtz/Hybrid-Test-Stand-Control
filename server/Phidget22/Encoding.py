import sys
import ctypes
class Encoding:
	# Unknown - the default value
	IR_ENCODING_UNKNOWN = 1
	# Space encoding, or Pulse Distance Modulation
	IR_ENCODING_SPACE = 2
	# Pulse encoding, or Pulse Width Modulation
	IR_ENCODING_PULSE = 3
	# Bi-Phase, or Manchester encoding
	IR_ENCODING_BIPHASE = 4
	# RC5 - a type of Bi-Phase encoding
	IR_ENCODING_RC5 = 5
	# RC6 - a type of Bi-Phase encoding
	IR_ENCODING_RC6 = 6

	@classmethod
	def getName(self, val):
		if val == self.IR_ENCODING_UNKNOWN:
			return "IR_ENCODING_UNKNOWN"
		if val == self.IR_ENCODING_SPACE:
			return "IR_ENCODING_SPACE"
		if val == self.IR_ENCODING_PULSE:
			return "IR_ENCODING_PULSE"
		if val == self.IR_ENCODING_BIPHASE:
			return "IR_ENCODING_BIPHASE"
		if val == self.IR_ENCODING_RC5:
			return "IR_ENCODING_RC5"
		if val == self.IR_ENCODING_RC6:
			return "IR_ENCODING_RC6"
		return "<invalid enumeration value>"
