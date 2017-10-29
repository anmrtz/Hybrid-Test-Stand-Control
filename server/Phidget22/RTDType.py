import sys
import ctypes
class RTDType:
	# Configures the RTD type as a PT100 with a 3850ppm curve.
	RTD_TYPE_PT100_3850 = 1
	# Configures the RTD type as a PT1000 with a 3850ppm curve.
	RTD_TYPE_PT1000_3850 = 2
	# Configures the RTD type as a PT100 with a 3920ppm curve.
	RTD_TYPE_PT100_3920 = 3
	# Configures the RTD type as a PT1000 with a 3920ppm curve.
	RTD_TYPE_PT1000_3920 = 4

	@classmethod
	def getName(self, val):
		if val == self.RTD_TYPE_PT100_3850:
			return "RTD_TYPE_PT100_3850"
		if val == self.RTD_TYPE_PT1000_3850:
			return "RTD_TYPE_PT1000_3850"
		if val == self.RTD_TYPE_PT100_3920:
			return "RTD_TYPE_PT100_3920"
		if val == self.RTD_TYPE_PT1000_3920:
			return "RTD_TYPE_PT1000_3920"
		return "<invalid enumeration value>"
