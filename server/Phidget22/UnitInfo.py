import sys
import ctypes

from Phidget22.Unit import Unit

class UnitInfo(ctypes.Structure):
	_fields_ = [
		("_unit", ctypes.c_int),
		("_name", ctypes.c_char_p),
		("_symbol", ctypes.c_char_p),
	]

	def __init__(self):
		self.unit = 0
		self.name = ""
		self.symbol = ""

	def fromPython(self):
		self._unit = self.unit
		self._name = self.name.encode('utf-8')
		self._symbol = self.symbol.encode('utf-8')
		return self

	def toPython(self):
		if self._unit == None:
			self.unit = None
		else:
			self.unit = self._unit
		if self._name == None:
			self.name = None
		else:
			self.name = self._name.decode('utf-8')
		if self._symbol == None:
			self.symbol = None
		else:
			self.symbol = self._symbol.decode('utf-8')
		return self
