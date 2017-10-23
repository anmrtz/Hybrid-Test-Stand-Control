import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Magnetometer(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._MagneticFieldChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_double)
		else:
			self._MagneticFieldChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.c_double)
		self._MagneticFieldChange = None
		self._onMagneticFieldChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localMagneticFieldChangeEvent(self, handle, userPtr, magneticField, timestamp):
		if self._MagneticFieldChange == None:
			return
		self._MagneticFieldChange(self, magneticField, timestamp)

	def setOnMagneticFieldChangeHandler(self, handler):
		if handler == None:
			self._MagneticFieldChange = None
			self._onMagneticFieldChange = None
		else:
			self._MagneticFieldChange = handler
			self._onMagneticFieldChange = self._MagneticFieldChangeFactory(self._localMagneticFieldChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_setOnMagneticFieldChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onMagneticFieldChange, None)
		except RuntimeError:
			self._MagneticFieldChange = None
			self._onMagneticFieldChange = None

	def getAxisCount(self):
		_AxisCount = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getAxisCount
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_AxisCount))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _AxisCount.value

	def setCorrectionParameters(self, magField, offset0, offset1, offset2, gain0, gain1, gain2, T0, T1, T2, T3, T4, T5):
		_magField = ctypes.c_double(magField)
		_offset0 = ctypes.c_double(offset0)
		_offset1 = ctypes.c_double(offset1)
		_offset2 = ctypes.c_double(offset2)
		_gain0 = ctypes.c_double(gain0)
		_gain1 = ctypes.c_double(gain1)
		_gain2 = ctypes.c_double(gain2)
		_T0 = ctypes.c_double(T0)
		_T1 = ctypes.c_double(T1)
		_T2 = ctypes.c_double(T2)
		_T3 = ctypes.c_double(T3)
		_T4 = ctypes.c_double(T4)
		_T5 = ctypes.c_double(T5)

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_setCorrectionParameters
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _magField, _offset0, _offset1, _offset2, _gain0, _gain1, _gain2, _T0, _T1, _T2, _T3, _T4, _T5)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getMagneticField(self):
		_MagneticField = (ctypes.c_double * 3)()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMagneticField
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MagneticField))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return list(_MagneticField)

	def getMinMagneticField(self):
		_MinMagneticField = (ctypes.c_double * 3)()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMinMagneticField
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinMagneticField))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return list(_MinMagneticField)

	def getMaxMagneticField(self):
		_MaxMagneticField = (ctypes.c_double * 3)()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMaxMagneticField
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxMagneticField))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return list(_MaxMagneticField)

	def getMagneticFieldChangeTrigger(self):
		_MagneticFieldChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMagneticFieldChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MagneticFieldChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MagneticFieldChangeTrigger.value

	def setMagneticFieldChangeTrigger(self, MagneticFieldChangeTrigger):
		_MagneticFieldChangeTrigger = ctypes.c_double(MagneticFieldChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_setMagneticFieldChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _MagneticFieldChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinMagneticFieldChangeTrigger(self):
		_MinMagneticFieldChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMinMagneticFieldChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinMagneticFieldChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinMagneticFieldChangeTrigger.value

	def getMaxMagneticFieldChangeTrigger(self):
		_MaxMagneticFieldChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getMaxMagneticFieldChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxMagneticFieldChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxMagneticFieldChangeTrigger.value

	def resetCorrectionParameters(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_resetCorrectionParameters
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def saveCorrectionParameters(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_saveCorrectionParameters
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getTimestamp(self):
		_Timestamp = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMagnetometer_getTimestamp
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Timestamp))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Timestamp.value
