import sys
import ctypes

from Phidget22.PhidgetServerType import PhidgetServerType

class PhidgetServer(ctypes.Structure):
	_fields_ = [
		("_name", ctypes.c_char_p),
		("_stype", ctypes.c_char_p),
		("_type", ctypes.c_int),
		("_flags", ctypes.c_int),
		("_addr", ctypes.c_char_p),
		("_host", ctypes.c_char_p),
		("_port", ctypes.c_int),
	]

	def __init__(self):
		self.name = ""
		self.stype = ""
		self.type = 0
		self.flags = 0
		self.addr = ""
		self.host = ""
		self.port = 0

	def fromPython(self):
		self._name = self.name.encode('utf-8')
		self._stype = self.stype.encode('utf-8')
		self._type = self.type
		self._flags = self.flags
		self._addr = self.addr.encode('utf-8')
		self._host = self.host.encode('utf-8')
		self._port = self.port
		return self

	def toPython(self):
		if self._name == None:
			self.name = None
		else:
			self.name = self._name.decode('utf-8')
		if self._stype == None:
			self.stype = None
		else:
			self.stype = self._stype.decode('utf-8')
		if self._type == None:
			self.type = None
		else:
			self.type = self._type
		if self._flags == None:
			self.flags = None
		else:
			self.flags = self._flags
		if self._addr == None:
			self.addr = None
		else:
			self.addr = self._addr.decode('utf-8')
		if self._host == None:
			self.host = None
		else:
			self.host = self._host.decode('utf-8')
		if self._port == None:
			self.port = None
		else:
			self.port = self._port
		return self
