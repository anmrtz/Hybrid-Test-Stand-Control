import sys
import ctypes


class GPSDate(ctypes.Structure):
	_fields_ = [
		("_tm_mday", ctypes.c_int16),
		("_tm_mon", ctypes.c_int16),
		("_tm_year", ctypes.c_int16),
	]

	def __init__(self):
		self.tm_mday = 0
		self.tm_mon = 0
		self.tm_year = 0

	def fromPython(self):
		self._tm_mday = self.tm_mday
		self._tm_mon = self.tm_mon
		self._tm_year = self.tm_year
		return self

	def toPython(self):
		if self._tm_mday == None:
			self.tm_mday = None
		else:
			self.tm_mday = self._tm_mday
		if self._tm_mon == None:
			self.tm_mon = None
		else:
			self.tm_mon = self._tm_mon
		if self._tm_year == None:
			self.tm_year = None
		else:
			self.tm_year = self._tm_year
		return self
