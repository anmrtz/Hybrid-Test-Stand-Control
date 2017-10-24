import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Dictionary(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._AddFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)
		else:
			self._AddFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)
		self._Add = None
		self._onAdd = None

		if sys.platform == 'win32':
			self._RemoveFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)
		else:
			self._RemoveFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p)
		self._Remove = None
		self._onRemove = None

		if sys.platform == 'win32':
			self._UpdateFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)
		else:
			self._UpdateFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p)
		self._Update = None
		self._onUpdate = None

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localAddEvent(self, handle, userPtr, key, value):
		if self._Add == None:
			return
		key = key.decode('utf-8')
		value = value.decode('utf-8')
		self._Add(self, key, value)

	def setOnAddHandler(self, handler):
		if handler == None:
			self._Add = None
			self._onAdd = None
		else:
			self._Add = handler
			self._onAdd = self._AddFactory(self._localAddEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_setOnAddHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onAdd, None)
		except RuntimeError:
			self._Add = None
			self._onAdd = None

	def _localRemoveEvent(self, handle, userPtr, key):
		if self._Remove == None:
			return
		key = key.decode('utf-8')
		self._Remove(self, key)

	def setOnRemoveHandler(self, handler):
		if handler == None:
			self._Remove = None
			self._onRemove = None
		else:
			self._Remove = handler
			self._onRemove = self._RemoveFactory(self._localRemoveEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_setOnRemoveHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onRemove, None)
		except RuntimeError:
			self._Remove = None
			self._onRemove = None

	def _localUpdateEvent(self, handle, userPtr, key, value):
		if self._Update == None:
			return
		key = key.decode('utf-8')
		value = value.decode('utf-8')
		self._Update(self, key, value)

	def setOnUpdateHandler(self, handler):
		if handler == None:
			self._Update = None
			self._onUpdate = None
		else:
			self._Update = handler
			self._onUpdate = self._UpdateFactory(self._localUpdateEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_setOnUpdateHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onUpdate, None)
		except RuntimeError:
			self._Update = None
			self._onUpdate = None

	def add(self, key, value):
		_key = ctypes.create_string_buffer(key.encode('utf-8'))
		_value = ctypes.create_string_buffer(value.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_add
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_key), ctypes.byref(_value))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def removeAll(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_removeAll
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def get(self, key):
		_key = ctypes.create_string_buffer(key.encode('utf-8'))
		_value = (ctypes.c_char * 65536)()
		_len = ctypes.c_int32(65536)

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_get
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_key), ctypes.byref(_value), _len)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _value.value.decode('utf-8')

	def remove(self, key):
		_key = ctypes.create_string_buffer(key.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_remove
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_key))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def scan(self, start):
		_start = ctypes.create_string_buffer(start.encode('utf-8'))
		_keyslist = (ctypes.c_char * 65536)()
		_len = ctypes.c_int32(65536)

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_scan
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_start), ctypes.byref(_keyslist), _len)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _keyslist.value.decode('utf-8')

	def set(self, key, value):
		_key = ctypes.create_string_buffer(key.encode('utf-8'))
		_value = ctypes.create_string_buffer(value.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_set
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_key), ctypes.byref(_value))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def update(self, key, value):
		_key = ctypes.create_string_buffer(key.encode('utf-8'))
		_value = ctypes.create_string_buffer(value.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetDictionary_update
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_key), ctypes.byref(_value))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

