import sys
import ctypes
class LCDPixelState:
	# Pixel off state
	PIXEL_STATE_OFF = 0
	# Pixel on state
	PIXEL_STATE_ON = 1
	# Invert the pixel state
	PIXEL_STATE_INVERT = 2

	@classmethod
	def getName(self, val):
		if val == self.PIXEL_STATE_OFF:
			return "PIXEL_STATE_OFF"
		if val == self.PIXEL_STATE_ON:
			return "PIXEL_STATE_ON"
		if val == self.PIXEL_STATE_INVERT:
			return "PIXEL_STATE_INVERT"
		return "<invalid enumeration value>"
