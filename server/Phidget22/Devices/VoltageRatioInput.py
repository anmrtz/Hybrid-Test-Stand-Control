import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.BridgeGain import BridgeGain
from Phidget22.VoltageRatioSensorType import VoltageRatioSensorType
from Phidget22.UnitInfo import UnitInfo
from Phidget22.Unit import Unit
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class VoltageRatioInput(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._SensorChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(UnitInfo))
		else:
			self._SensorChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.POINTER(UnitInfo))
		self._SensorChange = None
		self._onSensorChange = None

		if sys.platform == 'win32':
			self._VoltageRatioChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._VoltageRatioChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._VoltageRatioChange = None
		self._onVoltageRatioChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localSensorChangeEvent(self, handle, userPtr, sensorValue, sensorUnit):
		if self._SensorChange == None:
			return
		if sensorUnit != None:
			sensorUnit = sensorUnit.contents
			sensorUnit.toPython()
		self._SensorChange(self, sensorValue, sensorUnit)

	def setOnSensorChangeHandler(self, handler):
		if handler == None:
			self._SensorChange = None
			self._onSensorChange = None
		else:
			self._SensorChange = handler
			self._onSensorChange = self._SensorChangeFactory(self._localSensorChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setOnSensorChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onSensorChange, None)
		except RuntimeError:
			self._SensorChange = None
			self._onSensorChange = None

	def _localVoltageRatioChangeEvent(self, handle, userPtr, voltageRatio):
		if self._VoltageRatioChange == None:
			return
		self._VoltageRatioChange(self, voltageRatio)

	def setOnVoltageRatioChangeHandler(self, handler):
		if handler == None:
			self._VoltageRatioChange = None
			self._onVoltageRatioChange = None
		else:
			self._VoltageRatioChange = handler
			self._onVoltageRatioChange = self._VoltageRatioChangeFactory(self._localVoltageRatioChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setOnVoltageRatioChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onVoltageRatioChange, None)
		except RuntimeError:
			self._VoltageRatioChange = None
			self._onVoltageRatioChange = None

	def getBridgeEnabled(self):
		_BridgeEnabled = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getBridgeEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_BridgeEnabled))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _BridgeEnabled.value

	def setBridgeEnabled(self, BridgeEnabled):
		_BridgeEnabled = ctypes.c_int(BridgeEnabled)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setBridgeEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _BridgeEnabled)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getBridgeGain(self):
		_BridgeGain = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getBridgeGain
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_BridgeGain))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _BridgeGain.value

	def setBridgeGain(self, BridgeGain):
		_BridgeGain = ctypes.c_int(BridgeGain)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setBridgeGain
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _BridgeGain)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getSensorType(self):
		_SensorType = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getSensorType
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_SensorType))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _SensorType.value

	def setSensorType(self, SensorType):
		_SensorType = ctypes.c_int(SensorType)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setSensorType
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _SensorType)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getSensorUnit(self):
		_SensorUnit = UnitInfo()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getSensorUnit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_SensorUnit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _SensorUnit.toPython()

	def getSensorValue(self):
		_SensorValue = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getSensorValue
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_SensorValue))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _SensorValue.value

	def getSensorValueChangeTrigger(self):
		_SensorValueChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getSensorValueChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_SensorValueChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _SensorValueChangeTrigger.value

	def setSensorValueChangeTrigger(self, SensorValueChangeTrigger):
		_SensorValueChangeTrigger = ctypes.c_double(SensorValueChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setSensorValueChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _SensorValueChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getVoltageRatio(self):
		_VoltageRatio = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getVoltageRatio
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_VoltageRatio))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _VoltageRatio.value

	def getMinVoltageRatio(self):
		_MinVoltageRatio = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getMinVoltageRatio
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinVoltageRatio))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinVoltageRatio.value

	def getMaxVoltageRatio(self):
		_MaxVoltageRatio = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getMaxVoltageRatio
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxVoltageRatio))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxVoltageRatio.value

	def getVoltageRatioChangeTrigger(self):
		_VoltageRatioChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getVoltageRatioChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_VoltageRatioChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _VoltageRatioChangeTrigger.value

	def setVoltageRatioChangeTrigger(self, VoltageRatioChangeTrigger):
		_VoltageRatioChangeTrigger = ctypes.c_double(VoltageRatioChangeTrigger)

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_setVoltageRatioChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _VoltageRatioChangeTrigger)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinVoltageRatioChangeTrigger(self):
		_MinVoltageRatioChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getMinVoltageRatioChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinVoltageRatioChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinVoltageRatioChangeTrigger.value

	def getMaxVoltageRatioChangeTrigger(self):
		_MaxVoltageRatioChangeTrigger = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetVoltageRatioInput_getMaxVoltageRatioChangeTrigger
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxVoltageRatioChangeTrigger))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxVoltageRatioChangeTrigger.value
