import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.ErrorEventCode import ErrorEventCode

class PhidgetException(Exception):

	def __init__(self,code):
		_code = ctypes.c_int(code)
		_desc = ctypes.c_char_p()

		try:
				result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)
		
		self.code = code
		self.details = _desc.value.decode("utf-8");
		
	def __del__(self):
		pass
