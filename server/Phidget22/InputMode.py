import sys
import ctypes
class InputMode:
	# For interfacing NPN digital sensors
	INPUT_MODE_NPN = 1
	# For interfacing PNP digital sensors
	INPUT_MODE_PNP = 2

	@classmethod
	def getName(self, val):
		if val == self.INPUT_MODE_NPN:
			return "INPUT_MODE_NPN"
		if val == self.INPUT_MODE_PNP:
			return "INPUT_MODE_PNP"
		return "<invalid enumeration value>"
