import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Hub(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		try:
			__func = PhidgetSupport.getDll().PhidgetHub_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def setPortPower(self, port, state):
		_port = ctypes.c_int(port)
		_state = ctypes.c_int(state)

		try:
			__func = PhidgetSupport.getDll().PhidgetHub_setPortPower
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _port, _state)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

