import sys
import ctypes
class EncoderIOMode:
	# No additional pull-up or pull-down resistors will be applied to the input lines.
	ENCODER_IO_MODE_PUSH_PULL = 1
	# 2.2kΩ pull-down resistors will be applied to the input lines.
	ENCODER_IO_MODE_LINE_DRIVER_2K2 = 2
	# 10kΩ pull-down resistors will be applied to the input lines.
	ENCODER_IO_MODE_LINE_DRIVER_10K = 3
	# 2.2kΩ pull-up resistors will be applied to the input lines.
	ENCODER_IO_MODE_OPEN_COLLECTOR_2K2 = 4
	# 10kΩ pull-up resistors will be applied to the input lines.
	ENCODER_IO_MODE_OPEN_COLLECTOR_10K = 5

	@classmethod
	def getName(self, val):
		if val == self.ENCODER_IO_MODE_PUSH_PULL:
			return "ENCODER_IO_MODE_PUSH_PULL"
		if val == self.ENCODER_IO_MODE_LINE_DRIVER_2K2:
			return "ENCODER_IO_MODE_LINE_DRIVER_2K2"
		if val == self.ENCODER_IO_MODE_LINE_DRIVER_10K:
			return "ENCODER_IO_MODE_LINE_DRIVER_10K"
		if val == self.ENCODER_IO_MODE_OPEN_COLLECTOR_2K2:
			return "ENCODER_IO_MODE_OPEN_COLLECTOR_2K2"
		if val == self.ENCODER_IO_MODE_OPEN_COLLECTOR_10K:
			return "ENCODER_IO_MODE_OPEN_COLLECTOR_10K"
		return "<invalid enumeration value>"
