import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Manager:

	def __init__(self):
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._AttachFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
		else:
			self._AttachFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
		self._Attach = None
		self._onAttach = None

		if sys.platform == 'win32':
			self._DetachFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
		else:
			self._DetachFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p)
		self._Detach = None
		self._onDetach = None

		try:
			__func = PhidgetSupport.getDll().PhidgetManager_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetManager_delete
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise
		self.handle = None
		if res > 0:
			raise PhidgetException(res)

	def _localAttachEvent(self, handle, userPtr, Channel):
		if self._Attach == None:
			return
		try:
			__func = PhidgetSupport.getDll().Phidget_retain
			__func.restype = ctypes.c_int32
			result = __func(ctypes.c_void_p(Channel))
		except RuntimeError:
			raise
		if result > 0:
			raise PhidgetException(result)
		ph = Phidget()
		ph.handle = ctypes.c_void_p(Channel)
		self._Attach(self, ph)

	def setOnAttachHandler(self, handler):
		if handler == None:
			self._Attach = None
			self._onAttach = None
		else:
			self._Attach = handler
			self._onAttach = self._AttachFactory(self._localAttachEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetManager_setOnAttachHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onAttach, None)
		except RuntimeError:
			self._Attach = None
			self._onAttach = None

	def _localDetachEvent(self, handle, userPtr, Channel):
		if self._Detach == None:
			return
		try:
			__func = PhidgetSupport.getDll().Phidget_retain
			__func.restype = ctypes.c_int32
			result = __func(ctypes.c_void_p(Channel))
		except RuntimeError:
			raise
		if result > 0:
			raise PhidgetException(result)
		ph = Phidget()
		ph.handle = ctypes.c_void_p(Channel)
		self._Detach(self, ph)

	def setOnDetachHandler(self, handler):
		if handler == None:
			self._Detach = None
			self._onDetach = None
		else:
			self._Detach = handler
			self._onDetach = self._DetachFactory(self._localDetachEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetManager_setOnDetachHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onDetach, None)
		except RuntimeError:
			self._Detach = None
			self._onDetach = None

	def close(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetManager_close
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def open(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetManager_open
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

