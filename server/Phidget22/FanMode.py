import sys
import ctypes
class FanMode:
	# Turns the fan off.
	FAN_MODE_OFF = 1
	# Turns the fan on.
	FAN_MODE_ON = 2
	# The fan will be automatically controlled based on temperature.
	FAN_MODE_AUTO = 3

	@classmethod
	def getName(self, val):
		if val == self.FAN_MODE_OFF:
			return "FAN_MODE_OFF"
		if val == self.FAN_MODE_ON:
			return "FAN_MODE_ON"
		if val == self.FAN_MODE_AUTO:
			return "FAN_MODE_AUTO"
		return "<invalid enumeration value>"
