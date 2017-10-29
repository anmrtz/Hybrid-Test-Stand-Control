import sys
import ctypes
class PortMode:
	# Communicate with a smart VINT device
	PORT_MODE_VINT_PORT = 0
	# 5V Logic-level digital input
	PORT_MODE_DIGITAL_INPUT = 1
	# 3.3V digital output
	PORT_MODE_DIGITAL_OUTPUT = 2
	# 0-5V voltage input for non-ratiometric sensors 
	PORT_MODE_VOLTAGE_INPUT = 3
	# 0-5V voltage input for ratiometric sensors
	PORT_MODE_VOLTAGE_RATIO_INPUT = 4

	@classmethod
	def getName(self, val):
		if val == self.PORT_MODE_VINT_PORT:
			return "PORT_MODE_VINT_PORT"
		if val == self.PORT_MODE_DIGITAL_INPUT:
			return "PORT_MODE_DIGITAL_INPUT"
		if val == self.PORT_MODE_DIGITAL_OUTPUT:
			return "PORT_MODE_DIGITAL_OUTPUT"
		if val == self.PORT_MODE_VOLTAGE_INPUT:
			return "PORT_MODE_VOLTAGE_INPUT"
		if val == self.PORT_MODE_VOLTAGE_RATIO_INPUT:
			return "PORT_MODE_VOLTAGE_RATIO_INPUT"
		return "<invalid enumeration value>"
