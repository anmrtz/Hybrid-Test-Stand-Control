import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class DataAdapter(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._asyncFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		else:
			self._asyncFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)

		self._sendPacket_async = None
		self._onsendPacket_async = None

		if sys.platform == 'win32':
			self._PacketFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int32, ctypes.c_int)
		else:
			self._PacketFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_int32, ctypes.c_int)
		self._Packet = None
		self._onPacket = None

		try:
			__func = PhidgetSupport.getDll().PhidgetDataAdapter_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localPacketEvent(self, handle, userPtr, data, length, overrun):
		if self._Packet == None:
			return
		self._Packet(self, data, length, overrun)

	def setOnPacketHandler(self, handler):
		if handler == None:
			self._Packet = None
			self._onPacket = None
		else:
			self._Packet = handler
			self._onPacket = self._PacketFactory(self._localPacketEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDataAdapter_setOnPacketHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPacket, None)
		except RuntimeError:
			self._Packet = None
			self._onPacket = None

	def getMaxPacketLength(self):
		_MaxPacketLength = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetDataAdapter_getMaxPacketLength
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPacketLength))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPacketLength.value

	def sendPacket(self, data):
		_data = (ctypes.c_uint8 * len(data))(*data)
		_length = ctypes.c_int32(undefined)

		try:
			__func = PhidgetSupport.getDll().PhidgetDataAdapter_sendPacket
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_data), _length)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localsendPacket_async(self, handle, ctx, res):

		if self._sendPacket_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._sendPacket_async(self, res, details)

	def sendPacket_async(self, data, asyncHandler, ctx, fptr):
		if fptr == None:
			self._sendPacket_async = None
			self._onsendPacket_async = None
		else:
			self._sendPacket_async = fptr
			self._onsendPacket_async = self._asyncFactory(self._localsendPacket_async)

		_data = (ctypes.c_uint8 * len(data))(*data)
		_length = ctypes.c_int32(undefined)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_sendPacket_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsendPacket_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)
