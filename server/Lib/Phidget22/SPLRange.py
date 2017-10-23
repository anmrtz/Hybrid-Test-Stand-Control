import sys
import ctypes
class SPLRange:
	# Range 102dB
	SPL_RANGE_102dB = 1
	# Range 82dB
	SPL_RANGE_82dB = 2

	@classmethod
	def getName(self, val):
		if val == self.SPL_RANGE_102dB:
			return "SPL_RANGE_102dB"
		if val == self.SPL_RANGE_82dB:
			return "SPL_RANGE_82dB"
		return "<invalid enumeration value>"
