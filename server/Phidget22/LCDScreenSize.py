import sys
import ctypes
class LCDScreenSize:
	# Screen size unknown
	SCREEN_SIZE_NONE = 1
	# One row, eight column text screen
	SCREEN_SIZE_1x8 = 2
	# Two row, eight column text screen
	SCREEN_SIZE_2x8 = 3
	# One row, 16 column text screen
	SCREEN_SIZE_1x16 = 4
	# Two row, 16 column text screen
	SCREEN_SIZE_2x16 = 5
	# Four row, 16 column text screen
	SCREEN_SIZE_4x16 = 6
	# Two row, 20 column text screen
	SCREEN_SIZE_2x20 = 7
	# Four row, 20 column text screen.
	SCREEN_SIZE_4x20 = 8
	# Two row, 24 column text screen
	SCREEN_SIZE_2x24 = 9
	# One row, 40 column text screen
	SCREEN_SIZE_1x40 = 10
	# Two row, 40 column text screen
	SCREEN_SIZE_2x40 = 11
	# Four row, 40 column text screen
	SCREEN_SIZE_4x40 = 12
	# 64px by 128px graphic screen
	SCREEN_SIZE_64x128 = 13

	@classmethod
	def getName(self, val):
		if val == self.SCREEN_SIZE_NONE:
			return "SCREEN_SIZE_NONE"
		if val == self.SCREEN_SIZE_1x8:
			return "SCREEN_SIZE_1x8"
		if val == self.SCREEN_SIZE_2x8:
			return "SCREEN_SIZE_2x8"
		if val == self.SCREEN_SIZE_1x16:
			return "SCREEN_SIZE_1x16"
		if val == self.SCREEN_SIZE_2x16:
			return "SCREEN_SIZE_2x16"
		if val == self.SCREEN_SIZE_4x16:
			return "SCREEN_SIZE_4x16"
		if val == self.SCREEN_SIZE_2x20:
			return "SCREEN_SIZE_2x20"
		if val == self.SCREEN_SIZE_4x20:
			return "SCREEN_SIZE_4x20"
		if val == self.SCREEN_SIZE_2x24:
			return "SCREEN_SIZE_2x24"
		if val == self.SCREEN_SIZE_1x40:
			return "SCREEN_SIZE_1x40"
		if val == self.SCREEN_SIZE_2x40:
			return "SCREEN_SIZE_2x40"
		if val == self.SCREEN_SIZE_4x40:
			return "SCREEN_SIZE_4x40"
		if val == self.SCREEN_SIZE_64x128:
			return "SCREEN_SIZE_64x128"
		return "<invalid enumeration value>"
