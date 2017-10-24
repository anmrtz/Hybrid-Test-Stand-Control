import sys
import ctypes
class BridgeGain:
	# 1x Amplificaion
	BRIDGE_GAIN_1 = 1
	# 2x Amplification
	BRIDGE_GAIN_2 = 2
	# 4x Amplification
	BRIDGE_GAIN_4 = 3
	# 8x Amplification
	BRIDGE_GAIN_8 = 4
	# 16x Amplification
	BRIDGE_GAIN_16 = 5
	# 32x Amplification
	BRIDGE_GAIN_32 = 6
	# 64x Amplification
	BRIDGE_GAIN_64 = 7
	# 128x Amplification
	BRIDGE_GAIN_128 = 8

	@classmethod
	def getName(self, val):
		if val == self.BRIDGE_GAIN_1:
			return "BRIDGE_GAIN_1"
		if val == self.BRIDGE_GAIN_2:
			return "BRIDGE_GAIN_2"
		if val == self.BRIDGE_GAIN_4:
			return "BRIDGE_GAIN_4"
		if val == self.BRIDGE_GAIN_8:
			return "BRIDGE_GAIN_8"
		if val == self.BRIDGE_GAIN_16:
			return "BRIDGE_GAIN_16"
		if val == self.BRIDGE_GAIN_32:
			return "BRIDGE_GAIN_32"
		if val == self.BRIDGE_GAIN_64:
			return "BRIDGE_GAIN_64"
		if val == self.BRIDGE_GAIN_128:
			return "BRIDGE_GAIN_128"
		return "<invalid enumeration value>"
