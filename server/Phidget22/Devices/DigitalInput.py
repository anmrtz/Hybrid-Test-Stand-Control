import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.InputMode import InputMode
from Phidget22.PowerSupply import PowerSupply
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class DigitalInput(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._StateChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		else:
			self._StateChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		self._StateChange = None
		self._onStateChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localStateChangeEvent(self, handle, userPtr, state):
		if self._StateChange == None:
			return
		self._StateChange(self, state)

	def setOnStateChangeHandler(self, handler):
		if handler == None:
			self._StateChange = None
			self._onStateChange = None
		else:
			self._StateChange = handler
			self._onStateChange = self._StateChangeFactory(self._localStateChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_setOnStateChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onStateChange, None)
		except RuntimeError:
			self._StateChange = None
			self._onStateChange = None

	def getInputMode(self):
		_InputMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_getInputMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_InputMode))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _InputMode.value

	def setInputMode(self, InputMode):
		_InputMode = ctypes.c_int(InputMode)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_setInputMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _InputMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getPowerSupply(self):
		_PowerSupply = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_getPowerSupply
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PowerSupply))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PowerSupply.value

	def setPowerSupply(self, PowerSupply):
		_PowerSupply = ctypes.c_int(PowerSupply)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_setPowerSupply
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _PowerSupply)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getState(self):
		_State = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalInput_getState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_State))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _State.value
