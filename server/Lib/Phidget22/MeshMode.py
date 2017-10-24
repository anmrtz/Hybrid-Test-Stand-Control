import sys
import ctypes
class MeshMode:
	# Router mode
	MESHMODE_ROUTER = 1
	# Sleepy end device mode
	MESHMODE_SLEEPYENDDEVICE = 2

	@classmethod
	def getName(self, val):
		if val == self.MESHMODE_ROUTER:
			return "MESHMODE_ROUTER"
		if val == self.MESHMODE_SLEEPYENDDEVICE:
			return "MESHMODE_SLEEPYENDDEVICE"
		return "<invalid enumeration value>"
