import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.LEDForwardVoltage import LEDForwardVoltage
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class DigitalOutput(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._asyncFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		else:
			self._asyncFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)

		self._setDutyCycle_async = None
		self._onsetDutyCycle_async = None
		self._setLEDCurrentLimit_async = None
		self._onsetLEDCurrentLimit_async = None
		self._setState_async = None
		self._onsetState_async = None

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def getDutyCycle(self):
		_DutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_DutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _DutyCycle.value

	def setDutyCycle(self, DutyCycle):
		_DutyCycle = ctypes.c_double(DutyCycle)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DutyCycle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDutyCycle(self):
		_MinDutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMinDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinDutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinDutyCycle.value

	def getMaxDutyCycle(self):
		_MaxDutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMaxDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDutyCycle.value

	def _localsetDutyCycle_async(self, handle, ctx, res):

		if self._setDutyCycle_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._setDutyCycle_async(self, res, details)

	def setDutyCycle_async(self, DutyCycle, asyncHandler, ctx, fptr):
		if fptr == None:
			self._setDutyCycle_async = None
			self._onsetDutyCycle_async = None
		else:
			self._setDutyCycle_async = fptr
			self._onsetDutyCycle_async = self._asyncFactory(self._localsetDutyCycle_async)

		_DutyCycle = ctypes.c_double(DutyCycle)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setDutyCycle_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsetDutyCycle_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getLEDCurrentLimit(self):
		_LEDCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_LEDCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _LEDCurrentLimit.value

	def setLEDCurrentLimit(self, LEDCurrentLimit):
		_LEDCurrentLimit = ctypes.c_double(LEDCurrentLimit)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _LEDCurrentLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinLEDCurrentLimit(self):
		_MinLEDCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMinLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinLEDCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinLEDCurrentLimit.value

	def getMaxLEDCurrentLimit(self):
		_MaxLEDCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getMaxLEDCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxLEDCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxLEDCurrentLimit.value

	def _localsetLEDCurrentLimit_async(self, handle, ctx, res):

		if self._setLEDCurrentLimit_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._setLEDCurrentLimit_async(self, res, details)

	def setLEDCurrentLimit_async(self, LEDCurrentLimit, asyncHandler, ctx, fptr):
		if fptr == None:
			self._setLEDCurrentLimit_async = None
			self._onsetLEDCurrentLimit_async = None
		else:
			self._setLEDCurrentLimit_async = fptr
			self._onsetLEDCurrentLimit_async = self._asyncFactory(self._localsetLEDCurrentLimit_async)

		_LEDCurrentLimit = ctypes.c_double(LEDCurrentLimit)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setLEDCurrentLimit_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsetLEDCurrentLimit_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getLEDForwardVoltage(self):
		_LEDForwardVoltage = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getLEDForwardVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_LEDForwardVoltage))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _LEDForwardVoltage.value

	def setLEDForwardVoltage(self, LEDForwardVoltage):
		_LEDForwardVoltage = ctypes.c_int(LEDForwardVoltage)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setLEDForwardVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _LEDForwardVoltage)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getState(self):
		_State = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_getState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_State))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _State.value

	def setState(self, State):
		_State = ctypes.c_int(State)

		try:
			__func = PhidgetSupport.getDll().PhidgetDigitalOutput_setState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _State)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localsetState_async(self, handle, ctx, res):

		if self._setState_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._setState_async(self, res, details)

	def setState_async(self, State, asyncHandler, ctx, fptr):
		if fptr == None:
			self._setState_async = None
			self._onsetState_async = None
		else:
			self._setState_async = fptr
			self._onsetState_async = self._asyncFactory(self._localsetState_async)

		_State = ctypes.c_int(State)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setState_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsetState_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)
