import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class HumiditySensor(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._HumidityChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._HumidityChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._HumidityChange = None
		self._onHumidityChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localHumidityChangeEvent(self, handle, userPtr, humidity):
		if self._HumidityChange == None:
			return
		self._HumidityChange(self, humidity)

	def setOnHumidityChangeHandler(self, handler):
		if handler == None:
			self._HumidityChange = None
			self._onHumidityChange = None
		else:
			self._HumidityChange = handler
			self._onHumidityChange = self._HumidityChangeFactory(self._localHumidityChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_setOnHumidityChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onHumidityChange, None)
		except RuntimeError:
			self._HumidityChange = None
			self._onHumidityChange = None

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getHumidity(self):
		_Humidity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getHumidity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Humidity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Humidity.value

	def getMinHumidity(self):
		_MinHumidity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getMinHumidity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinHumidity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinHumidity.value

	def getMaxHumidity(self):
		_MaxHumidity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getMaxHumidity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxHumidity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxHumidity.value

	def getHumidityChangeTrigger(self):
		_HumidityChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getHumidityChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_HumidityChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _HumidityChangeTrigger.value

	def setHumidityChangeTrigger(self, HumidityChangeTrigger):
		_HumidityChangeTrigger = ctypes.c_double(HumidityChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_setHumidityChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _HumidityChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinHumidityChangeTrigger(self):
		_MinHumidityChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getMinHumidityChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinHumidityChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinHumidityChangeTrigger.value

	def getMaxHumidityChangeTrigger(self):
		_MaxHumidityChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetHumiditySensor_getMaxHumidityChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxHumidityChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxHumidityChangeTrigger.value
