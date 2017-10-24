import sys
import ctypes
class ControlMode:
	# Control the motor by setting a target position.
	CONTROL_MODE_STEP = 0
	# Control the motor by selecting a target velocity (sign indicates direction). The motor will rotate continously in the chosen direction.
	CONTROL_MODE_RUN = 1

	@classmethod
	def getName(self, val):
		if val == self.CONTROL_MODE_STEP:
			return "CONTROL_MODE_STEP"
		if val == self.CONTROL_MODE_RUN:
			return "CONTROL_MODE_RUN"
		return "<invalid enumeration value>"
