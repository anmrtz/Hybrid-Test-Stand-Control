import sys
import ctypes
class PhidgetServerType:
	# Unknown or unspecified server type
	PHIDGETSERVER_NONE = 0
	# Phidget22 Server listener
	PHIDGETSERVER_DEVICELISTENER = 1
	# Phidget22 Server connection
	PHIDGETSERVER_DEVICE = 2
	# Phidget22 Server
	PHIDGETSERVER_DEVICEREMOTE = 3
	# Phidget22 Web Server
	PHIDGETSERVER_WWWLISTENER = 4
	# Phidget22 Web Server connection
	PHIDGETSERVER_WWW = 5
	# Phidget22 Web server
	PHIDGETSERVER_WWWREMOTE = 6
	# Phidget SBC
	PHIDGETSERVER_SBC = 7

	@classmethod
	def getName(self, val):
		if val == self.PHIDGETSERVER_NONE:
			return "PHIDGETSERVER_NONE"
		if val == self.PHIDGETSERVER_DEVICELISTENER:
			return "PHIDGETSERVER_DEVICELISTENER"
		if val == self.PHIDGETSERVER_DEVICE:
			return "PHIDGETSERVER_DEVICE"
		if val == self.PHIDGETSERVER_DEVICEREMOTE:
			return "PHIDGETSERVER_DEVICEREMOTE"
		if val == self.PHIDGETSERVER_WWWLISTENER:
			return "PHIDGETSERVER_WWWLISTENER"
		if val == self.PHIDGETSERVER_WWW:
			return "PHIDGETSERVER_WWW"
		if val == self.PHIDGETSERVER_WWWREMOTE:
			return "PHIDGETSERVER_WWWREMOTE"
		if val == self.PHIDGETSERVER_SBC:
			return "PHIDGETSERVER_SBC"
		return "<invalid enumeration value>"
