import sys
import ctypes
class LCDFont:
	# User-defined font #1
	FONT_User1 = 1
	# User-defined font #2
	FONT_User2 = 2
	# 6px by 10px font
	FONT_6x10 = 3
	# 5px by 8px font
	FONT_5x8 = 4
	# 6px by 12px font
	FONT_6x12 = 5

	@classmethod
	def getName(self, val):
		if val == self.FONT_User1:
			return "FONT_User1"
		if val == self.FONT_User2:
			return "FONT_User2"
		if val == self.FONT_6x10:
			return "FONT_6x10"
		if val == self.FONT_5x8:
			return "FONT_5x8"
		if val == self.FONT_6x12:
			return "FONT_6x12"
		return "<invalid enumeration value>"
