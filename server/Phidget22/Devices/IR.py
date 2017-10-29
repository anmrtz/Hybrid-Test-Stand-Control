import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.CodeInfo import CodeInfo
from Phidget22.Encoding import Encoding
from Phidget22.Length import Length
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class IR(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._CodeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_int)
		else:
			self._CodeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_int)
		self._Code = None
		self._onCode = None

		if sys.platform == 'win32':
			self._LearnFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(CodeInfo))
		else:
			self._LearnFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.POINTER(CodeInfo))
		self._Learn = None
		self._onLearn = None

		if sys.platform == 'win32':
			self._RawDataFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32)
		else:
			self._RawDataFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_int32), ctypes.c_int32)
		self._RawData = None
		self._onRawData = None

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localCodeEvent(self, handle, userPtr, code, bitCount, isRepeat):
		if self._Code == None:
			return
		code = code.decode('utf-8')
		self._Code(self, code, bitCount, isRepeat)

	def setOnCodeHandler(self, handler):
		if handler == None:
			self._Code = None
			self._onCode = None
		else:
			self._Code = handler
			self._onCode = self._CodeFactory(self._localCodeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_setOnCodeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onCode, None)
		except RuntimeError:
			self._Code = None
			self._onCode = None

	def _localLearnEvent(self, handle, userPtr, code, codeInfo):
		if self._Learn == None:
			return
		code = code.decode('utf-8')
		if codeInfo != None:
			codeInfo = codeInfo.contents
			codeInfo.toPython()
		self._Learn(self, code, codeInfo)

	def setOnLearnHandler(self, handler):
		if handler == None:
			self._Learn = None
			self._onLearn = None
		else:
			self._Learn = handler
			self._onLearn = self._LearnFactory(self._localLearnEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_setOnLearnHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onLearn, None)
		except RuntimeError:
			self._Learn = None
			self._onLearn = None

	def _localRawDataEvent(self, handle, userPtr, data, dataLength):
		if self._RawData == None:
			return
		self._RawData(self, data, dataLength)

	def setOnRawDataHandler(self, handler):
		if handler == None:
			self._RawData = None
			self._onRawData = None
		else:
			self._RawData = handler
			self._onRawData = self._RawDataFactory(self._localRawDataEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_setOnRawDataHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onRawData, None)
		except RuntimeError:
			self._RawData = None
			self._onRawData = None

	def getLastCode(self):
		_code = (ctypes.c_char * 33)()
		_codeLength = ctypes.c_int32(33)
		_bitCount = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_getLastCode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_code), _codeLength, ctypes.byref(_bitCount))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _code.value.decode('utf-8'), _bitCount.value

	def getLastLearnedCode(self):
		_code = (ctypes.c_char * 33)()
		_codeLength = ctypes.c_int32(33)
		_codeInfo = CodeInfo()

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_getLastLearnedCode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_code), _codeLength, ctypes.byref(_codeInfo))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _code.value.decode('utf-8'), _codeInfo.toPython()

	def transmit(self, code, codeInfo):
		_code = ctypes.create_string_buffer(code.encode('utf-8'))
		_codeInfo = codeInfo.fromPython()

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_transmit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_code), ctypes.byref(_codeInfo))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def transmitRaw(self, data, carrierFrequency, dutyCycle, gap):
		_data = (ctypes.c_uint32 * len(data))(*data)
		_dataLength = ctypes.c_int32(undefined)
		_carrierFrequency = ctypes.c_uint32(carrierFrequency)
		_dutyCycle = ctypes.c_double(dutyCycle)
		_gap = ctypes.c_uint32(gap)

		try:
			__func = PhidgetSupport.getDll().PhidgetIR_transmitRaw
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_data), _dataLength, _carrierFrequency, _dutyCycle, _gap)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def transmitRepeat(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetIR_transmitRepeat
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

