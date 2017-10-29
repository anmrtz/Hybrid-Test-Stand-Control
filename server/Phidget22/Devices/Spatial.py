import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Spatial(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._SpatialDataFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_double)
		else:
			self._SpatialDataFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_double)
		self._SpatialData = None
		self._onSpatialData = None

		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localSpatialDataEvent(self, handle, userPtr, acceleration, angularRate, magneticField, timestamp):
		if self._SpatialData == None:
			return
		self._SpatialData(self, acceleration, angularRate, magneticField, timestamp)

	def setOnSpatialDataHandler(self, handler):
		if handler == None:
			self._SpatialData = None
			self._onSpatialData = None
		else:
			self._SpatialData = handler
			self._onSpatialData = self._SpatialDataFactory(self._localSpatialDataEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_setOnSpatialDataHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onSpatialData, None)
		except RuntimeError:
			self._SpatialData = None
			self._onSpatialData = None

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetSpatial_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetSpatial_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def setMagnetometerCorrectionParameters(self, magField, offset0, offset1, offset2, gain0, gain1, gain2, T0, T1, T2, T3, T4, T5):
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
			__func = PhidgetSupport.getDll().PhidgetSpatial_setMagnetometerCorrectionParameters
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _magField, _offset0, _offset1, _offset2, _gain0, _gain1, _gain2, _T0, _T1, _T2, _T3, _T4, _T5)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def resetMagnetometerCorrectionParameters(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_resetMagnetometerCorrectionParameters
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def saveMagnetometerCorrectionParameters(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_saveMagnetometerCorrectionParameters
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def zeroGyro(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetSpatial_zeroGyro
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

