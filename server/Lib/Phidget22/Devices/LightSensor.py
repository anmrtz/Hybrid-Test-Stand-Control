import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class LightSensor(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._IlluminanceChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._IlluminanceChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._IlluminanceChange = None
		self._onIlluminanceChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localIlluminanceChangeEvent(self, handle, userPtr, illuminance):
		if self._IlluminanceChange == None:
			return
		self._IlluminanceChange(self, illuminance)

	def setOnIlluminanceChangeHandler(self, handler):
		if handler == None:
			self._IlluminanceChange = None
			self._onIlluminanceChange = None
		else:
			self._IlluminanceChange = handler
			self._onIlluminanceChange = self._IlluminanceChangeFactory(self._localIlluminanceChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_setOnIlluminanceChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onIlluminanceChange, None)
		except RuntimeError:
			self._IlluminanceChange = None
			self._onIlluminanceChange = None

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetLightSensor_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getIlluminance(self):
		_Illuminance = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getIlluminance
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Illuminance))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Illuminance.value

	def getMinIlluminance(self):
		_MinIlluminance = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getMinIlluminance
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinIlluminance))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinIlluminance.value

	def getMaxIlluminance(self):
		_MaxIlluminance = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getMaxIlluminance
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxIlluminance))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxIlluminance.value

	def getIlluminanceChangeTrigger(self):
		_IlluminanceChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getIlluminanceChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_IlluminanceChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _IlluminanceChangeTrigger.value

	def setIlluminanceChangeTrigger(self, IlluminanceChangeTrigger):
		_IlluminanceChangeTrigger = ctypes.c_double(IlluminanceChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_setIlluminanceChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _IlluminanceChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinIlluminanceChangeTrigger(self):
		_MinIlluminanceChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getMinIlluminanceChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinIlluminanceChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinIlluminanceChangeTrigger.value

	def getMaxIlluminanceChangeTrigger(self):
		_MaxIlluminanceChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLightSensor_getMaxIlluminanceChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxIlluminanceChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxIlluminanceChangeTrigger.value
