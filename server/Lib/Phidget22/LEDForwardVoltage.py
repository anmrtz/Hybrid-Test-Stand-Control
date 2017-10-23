import sys
import ctypes
class LEDForwardVoltage:
	# 1.7 V
	LED_FORWARD_VOLTAGE_1_7V = 1
	# 2.75 V
	LED_FORWARD_VOLTAGE_2_75V = 2
	# 3.2 V
	LED_FORWARD_VOLTAGE_3_2V = 3
	# 3.9 V
	LED_FORWARD_VOLTAGE_3_9V = 4
	# 4.0 V
	LED_FORWARD_VOLTAGE_4_0V = 5
	# 4.8 V
	LED_FORWARD_VOLTAGE_4_8V = 6
	# 5.0 V
	LED_FORWARD_VOLTAGE_5_0V = 7
	# 5.6 V
	LED_FORWARD_VOLTAGE_5_6V = 8

	@classmethod
	def getName(self, val):
		if val == self.LED_FORWARD_VOLTAGE_1_7V:
			return "LED_FORWARD_VOLTAGE_1_7V"
		if val == self.LED_FORWARD_VOLTAGE_2_75V:
			return "LED_FORWARD_VOLTAGE_2_75V"
		if val == self.LED_FORWARD_VOLTAGE_3_2V:
			return "LED_FORWARD_VOLTAGE_3_2V"
		if val == self.LED_FORWARD_VOLTAGE_3_9V:
			return "LED_FORWARD_VOLTAGE_3_9V"
		if val == self.LED_FORWARD_VOLTAGE_4_0V:
			return "LED_FORWARD_VOLTAGE_4_0V"
		if val == self.LED_FORWARD_VOLTAGE_4_8V:
			return "LED_FORWARD_VOLTAGE_4_8V"
		if val == self.LED_FORWARD_VOLTAGE_5_0V:
			return "LED_FORWARD_VOLTAGE_5_0V"
		if val == self.LED_FORWARD_VOLTAGE_5_6V:
			return "LED_FORWARD_VOLTAGE_5_6V"
		return "<invalid enumeration value>"
