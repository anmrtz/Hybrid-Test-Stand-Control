import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.EncoderIOMode import EncoderIOMode
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Encoder(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._PositionChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_double, ctypes.c_int)
		else:
			self._PositionChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_double, ctypes.c_int)
		self._PositionChange = None
		self._onPositionChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localPositionChangeEvent(self, handle, userPtr, positionChange, timeChange, indexTriggered):
		if self._PositionChange == None:
			return
		self._PositionChange(self, positionChange, timeChange, indexTriggered)

	def setOnPositionChangeHandler(self, handler):
		if handler == None:
			self._PositionChange = None
			self._onPositionChange = None
		else:
			self._PositionChange = handler
			self._onPositionChange = self._PositionChangeFactory(self._localPositionChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def setEnabled(self, Enabled):
		_Enabled = ctypes.c_int(Enabled)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Enabled)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getEnabled(self):
		_Enabled = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Enabled))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Enabled.value

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_DataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _DataInterval.value

	def setDataInterval(self, DataInterval):
		_DataInterval = ctypes.c_uint32(DataInterval)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getMinDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinDataInterval.value

	def getMaxDataInterval(self):
		_MaxDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getIndexPosition(self):
		_IndexPosition = ctypes.c_int64()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getIndexPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_IndexPosition))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _IndexPosition.value

	def getIOMode(self):
		_IOMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getIOMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_IOMode))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _IOMode.value

	def setIOMode(self, IOMode):
		_IOMode = ctypes.c_int(IOMode)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setIOMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _IOMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getPosition(self):
		_Position = ctypes.c_int64()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Position))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Position.value

	def setPosition(self, Position):
		_Position = ctypes.c_int64(Position)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Position)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getPositionChangeTrigger(self):
		_PositionChangeTrigger = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getPositionChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PositionChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PositionChangeTrigger.value

	def setPositionChangeTrigger(self, PositionChangeTrigger):
		_PositionChangeTrigger = ctypes.c_uint32(PositionChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_setPositionChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _PositionChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinPositionChangeTrigger(self):
		_MinPositionChangeTrigger = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getMinPositionChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPositionChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPositionChangeTrigger.value

	def getMaxPositionChangeTrigger(self):
		_MaxPositionChangeTrigger = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetEncoder_getMaxPositionChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPositionChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPositionChangeTrigger.value
