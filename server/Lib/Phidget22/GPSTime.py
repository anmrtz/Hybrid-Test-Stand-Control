import sys
import ctypes


class GPSTime(ctypes.Structure):
	_fields_ = [
		("_tm_ms", ctypes.c_int16),
		("_tm_sec", ctypes.c_int16),
		("_tm_min", ctypes.c_int16),
		("_tm_hour", ctypes.c_int16),
	]

	def __init__(self):
		self.tm_ms = 0
		self.tm_sec = 0
		self.tm_min = 0
		self.tm_hour = 0

	def fromPython(self):
		self._tm_ms = self.tm_ms
		self._tm_sec = self.tm_sec
		self._tm_min = self.tm_min
		self._tm_hour = self.tm_hour
		return self

	def toPython(self):
		if self._tm_ms == None:
			self.tm_ms = None
		else:
			self.tm_ms = self._tm_ms
		if self._tm_sec == None:
			self.tm_sec = None
		else:
			self.tm_sec = self._tm_sec
		if self._tm_min == None:
			self.tm_min = None
		else:
			self.tm_min = self._tm_min
		if self._tm_hour == None:
			self.tm_hour = None
		else:
			self.tm_hour = self._tm_hour
		return self
