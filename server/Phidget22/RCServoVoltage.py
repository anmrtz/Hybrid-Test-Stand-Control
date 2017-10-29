import sys
import ctypes
class RCServoVoltage:
	# Run all servos on 5V DC
	RCSERVO_VOLTAGE_5V = 1
	# Run all servos on 6V DC
	RCSERVO_VOLTAGE_6V = 2
	# Run all servos on 7.4V DC
	RCSERVO_VOLTAGE_7_4V = 3

	@classmethod
	def getName(self, val):
		if val == self.RCSERVO_VOLTAGE_5V:
			return "RCSERVO_VOLTAGE_5V"
		if val == self.RCSERVO_VOLTAGE_6V:
			return "RCSERVO_VOLTAGE_6V"
		if val == self.RCSERVO_VOLTAGE_7_4V:
			return "RCSERVO_VOLTAGE_7_4V"
		return "<invalid enumeration value>"
