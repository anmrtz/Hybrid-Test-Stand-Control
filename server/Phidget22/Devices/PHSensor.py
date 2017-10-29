import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class PHSensor(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._PHChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._PHChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._PHChange = None
		self._onPHChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localPHChangeEvent(self, handle, userPtr, PH):
		if self._PHChange == None:
			return
		self._PHChange(self, PH)

	def setOnPHChangeHandler(self, handler):
		if handler == None:
			self._PHChange = None
			self._onPHChange = None
		else:
			self._PHChange = handler
			self._onPHChange = self._PHChangeFactory(self._localPHChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_setOnPHChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPHChange, None)
		except RuntimeError:
			self._PHChange = None
			self._onPHChange = None

	def getCorrectionTemperature(self):
		_CorrectionTemperature = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getCorrectionTemperature
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_CorrectionTemperature))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _CorrectionTemperature.value

	def setCorrectionTemperature(self, CorrectionTemperature):
		_CorrectionTemperature = ctypes.c_double(CorrectionTemperature)

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_setCorrectionTemperature
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _CorrectionTemperature)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinCorrectionTemperature(self):
		_MinCorrectionTemperature = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMinCorrectionTemperature
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinCorrectionTemperature))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinCorrectionTemperature.value

	def getMaxCorrectionTemperature(self):
		_MaxCorrectionTemperature = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMaxCorrectionTemperature
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxCorrectionTemperature))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxCorrectionTemperature.value

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetPHSensor_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getPH(self):
		_PH = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getPH
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PH))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PH.value

	def getMinPH(self):
		_MinPH = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMinPH
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPH))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPH.value

	def getMaxPH(self):
		_MaxPH = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMaxPH
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPH))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPH.value

	def getPHChangeTrigger(self):
		_PHChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getPHChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PHChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PHChangeTrigger.value

	def setPHChangeTrigger(self, PHChangeTrigger):
		_PHChangeTrigger = ctypes.c_double(PHChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_setPHChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _PHChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinPHChangeTrigger(self):
		_MinPHChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMinPHChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPHChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPHChangeTrigger.value

	def getMaxPHChangeTrigger(self):
		_MaxPHChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPHSensor_getMaxPHChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPHChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPHChangeTrigger.value
