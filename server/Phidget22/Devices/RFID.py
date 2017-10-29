import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.RFIDProtocol import RFIDProtocol
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class RFID(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._TagFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)
		else:
			self._TagFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)
		self._Tag = None
		self._onTag = None

		if sys.platform == 'win32':
			self._TagLostFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)
		else:
			self._TagLostFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int)
		self._TagLost = None
		self._onTagLost = None

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localTagEvent(self, handle, userPtr, Tag, Protocol):
		if self._Tag == None:
			return
		Tag = Tag.decode('utf-8')
		self._Tag(self, Tag, Protocol)

	def setOnTagHandler(self, handler):
		if handler == None:
			self._Tag = None
			self._onTag = None
		else:
			self._Tag = handler
			self._onTag = self._TagFactory(self._localTagEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_setOnTagHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onTag, None)
		except RuntimeError:
			self._Tag = None
			self._onTag = None

	def _localTagLostEvent(self, handle, userPtr, Tag, Protocol):
		if self._TagLost == None:
			return
		Tag = Tag.decode('utf-8')
		self._TagLost(self, Tag, Protocol)

	def setOnTagLostHandler(self, handler):
		if handler == None:
			self._TagLost = None
			self._onTagLost = None
		else:
			self._TagLost = handler
			self._onTagLost = self._TagLostFactory(self._localTagLostEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_setOnTagLostHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onTagLost, None)
		except RuntimeError:
			self._TagLost = None
			self._onTagLost = None

	def getAntennaEnabled(self):
		_AntennaEnabled = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_getAntennaEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_AntennaEnabled))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _AntennaEnabled.value

	def setAntennaEnabled(self, AntennaEnabled):
		_AntennaEnabled = ctypes.c_int(AntennaEnabled)

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_setAntennaEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _AntennaEnabled)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getLastTag(self):
		_tagString = (ctypes.c_char * 25)()
		_tagStringLen = ctypes.c_int32(25)
		_protocol = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_getLastTag
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_tagString), _tagStringLen, ctypes.byref(_protocol))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _tagString.value.decode('utf-8'), _protocol.value

	def getTagPresent(self):
		_TagPresent = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_getTagPresent
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_TagPresent))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _TagPresent.value

	def write(self, tagString, protocol, lockTag):
		_tagString = ctypes.create_string_buffer(tagString.encode('utf-8'))
		_protocol = ctypes.c_int(protocol)
		_lockTag = ctypes.c_int(lockTag)

		try:
			__func = PhidgetSupport.getDll().PhidgetRFID_write
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_tagString), _protocol, _lockTag)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

