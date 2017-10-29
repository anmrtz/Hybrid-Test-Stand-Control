import sys
import ctypes
class LogLevel:
	# Critical
	PHIDGET_LOG_CRITICAL = 1
	# Error
	PHIDGET_LOG_ERROR = 2
	# Warning
	PHIDGET_LOG_WARNING = 3
	# Info
	PHIDGET_LOG_INFO = 4
	# Debug
	PHIDGET_LOG_DEBUG = 5
	# Verbose
	PHIDGET_LOG_VERBOSE = 6

	@classmethod
	def getName(self, val):
		if val == self.PHIDGET_LOG_CRITICAL:
			return "PHIDGET_LOG_CRITICAL"
		if val == self.PHIDGET_LOG_ERROR:
			return "PHIDGET_LOG_ERROR"
		if val == self.PHIDGET_LOG_WARNING:
			return "PHIDGET_LOG_WARNING"
		if val == self.PHIDGET_LOG_INFO:
			return "PHIDGET_LOG_INFO"
		if val == self.PHIDGET_LOG_DEBUG:
			return "PHIDGET_LOG_DEBUG"
		if val == self.PHIDGET_LOG_VERBOSE:
			return "PHIDGET_LOG_VERBOSE"
		return "<invalid enumeration value>"
