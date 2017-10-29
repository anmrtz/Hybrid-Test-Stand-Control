import sys
import ctypes
class RTDWireSetup:
	# Configures the device to make resistance calculations based on a 2-wire RTD setup.
	RTD_WIRE_SETUP_2WIRE = 1
	# Configures the device to make resistance calculations based on a 3-wire RTD setup.
	RTD_WIRE_SETUP_3WIRE = 2
	# Configures the device to make resistance calculations based on a 4-wire RTD setup.
	RTD_WIRE_SETUP_4WIRE = 3

	@classmethod
	def getName(self, val):
		if val == self.RTD_WIRE_SETUP_2WIRE:
			return "RTD_WIRE_SETUP_2WIRE"
		if val == self.RTD_WIRE_SETUP_3WIRE:
			return "RTD_WIRE_SETUP_3WIRE"
		if val == self.RTD_WIRE_SETUP_4WIRE:
			return "RTD_WIRE_SETUP_4WIRE"
		return "<invalid enumeration value>"
