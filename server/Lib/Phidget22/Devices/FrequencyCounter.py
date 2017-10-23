import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.FilterType import FilterType
from Phidget22.InputMode import InputMode
from Phidget22.PowerSupply import PowerSupply
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class FrequencyCounter(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._CountChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_double)
		else:
			self._CountChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_uint64, ctypes.c_double)
		self._CountChange = None
		self._onCountChange = None

		if sys.platform == 'win32':
			self._FrequencyChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._FrequencyChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._FrequencyChange = None
		self._onFrequencyChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localCountChangeEvent(self, handle, userPtr, counts, timeChange):
		if self._CountChange == None:
			return
		self._CountChange(self, counts, timeChange)

	def setOnCountChangeHandler(self, handler):
		if handler == None:
			self._CountChange = None
			self._onCountChange = None
		else:
			self._CountChange = handler
			self._onCountChange = self._CountChangeFactory(self._localCountChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setOnCountChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onCountChange, None)
		except RuntimeError:
			self._CountChange = None
			self._onCountChange = None

	def _localFrequencyChangeEvent(self, handle, userPtr, frequency):
		if self._FrequencyChange == None:
			return
		self._FrequencyChange(self, frequency)

	def setOnFrequencyChangeHandler(self, handler):
		if handler == None:
			self._FrequencyChange = None
			self._onFrequencyChange = None
		else:
			self._FrequencyChange = handler
			self._onFrequencyChange = self._FrequencyChangeFactory(self._localFrequencyChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setOnFrequencyChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onFrequencyChange, None)
		except RuntimeError:
			self._FrequencyChange = None
			self._onFrequencyChange = None

	def getCount(self):
		_Count = ctypes.c_uint64()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getCount
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Count))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Count.value

	def getEnabled(self):
		_Enabled = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Enabled))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Enabled.value

	def setEnabled(self, Enabled):
		_Enabled = ctypes.c_int(Enabled)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Enabled)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getFilterType(self):
		_FilterType = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getFilterType
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_FilterType))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _FilterType.value

	def setFilterType(self, FilterType):
		_FilterType = ctypes.c_int(FilterType)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setFilterType
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _FilterType)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getFrequency(self):
		_Frequency = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getFrequency
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Frequency))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Frequency.value

	def getMaxFrequency(self):
		_MaxFrequency = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getMaxFrequency
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxFrequency))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxFrequency.value

	def getFrequencyCutoff(self):
		_FrequencyCutoff = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getFrequencyCutoff
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_FrequencyCutoff))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _FrequencyCutoff.value

	def setFrequencyCutoff(self, FrequencyCutoff):
		_FrequencyCutoff = ctypes.c_double(FrequencyCutoff)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setFrequencyCutoff
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _FrequencyCutoff)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinFrequencyCutoff(self):
		_MinFrequencyCutoff = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getMinFrequencyCutoff
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinFrequencyCutoff))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinFrequencyCutoff.value

	def getMaxFrequencyCutoff(self):
		_MaxFrequencyCutoff = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getMaxFrequencyCutoff
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxFrequencyCutoff))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxFrequencyCutoff.value

	def getInputMode(self):
		_InputMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getInputMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_InputMode))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _InputMode.value

	def setInputMode(self, InputMode):
		_InputMode = ctypes.c_int(InputMode)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setInputMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _InputMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getPowerSupply(self):
		_PowerSupply = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getPowerSupply
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PowerSupply))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PowerSupply.value

	def setPowerSupply(self, PowerSupply):
		_PowerSupply = ctypes.c_int(PowerSupply)

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_setPowerSupply
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _PowerSupply)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def reset(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_reset
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getTimeElapsed(self):
		_TimeElapsed = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetFrequencyCounter_getTimeElapsed
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_TimeElapsed))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _TimeElapsed.value
