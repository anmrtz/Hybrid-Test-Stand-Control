import sys
import ctypes
class ThermocoupleType:
	# Configures the thermocouple input as a J-Type thermocouple.
	THERMOCOUPLE_TYPE_J = 1
	# Configures the thermocouple input as a K-Type thermocouple.
	THERMOCOUPLE_TYPE_K = 2
	# Configures the thermocouple input as a E-Type thermocouple.
	THERMOCOUPLE_TYPE_E = 3
	# Configures the thermocouple input as a T-Type thermocouple.
	THERMOCOUPLE_TYPE_T = 4

	@classmethod
	def getName(self, val):
		if val == self.THERMOCOUPLE_TYPE_J:
			return "THERMOCOUPLE_TYPE_J"
		if val == self.THERMOCOUPLE_TYPE_K:
			return "THERMOCOUPLE_TYPE_K"
		if val == self.THERMOCOUPLE_TYPE_E:
			return "THERMOCOUPLE_TYPE_E"
		if val == self.THERMOCOUPLE_TYPE_T:
			return "THERMOCOUPLE_TYPE_T"
		return "<invalid enumeration value>"
