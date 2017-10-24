import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.FanMode import FanMode
from Phidget22.EncoderIOMode import EncoderIOMode
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class MotorPositionController(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._asyncFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		else:
			self._asyncFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)

		self._setTargetPosition_async = None
		self._onsetTargetPosition_async = None

		if sys.platform == 'win32':
			self._DutyCycleUpdateFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._DutyCycleUpdateFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._DutyCycleUpdate = None
		self._onDutyCycleUpdate = None

		if sys.platform == 'win32':
			self._PositionChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._PositionChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._PositionChange = None
		self._onPositionChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localDutyCycleUpdateEvent(self, handle, userPtr, dutyCycle):
		if self._DutyCycleUpdate == None:
			return
		self._DutyCycleUpdate(self, dutyCycle)

	def setOnDutyCycleUpdateHandler(self, handler):
		if handler == None:
			self._DutyCycleUpdate = None
			self._onDutyCycleUpdate = None
		else:
			self._DutyCycleUpdate = handler
			self._onDutyCycleUpdate = self._DutyCycleUpdateFactory(self._localDutyCycleUpdateEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setOnDutyCycleUpdateHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onDutyCycleUpdate, None)
		except RuntimeError:
			self._DutyCycleUpdate = None
			self._onDutyCycleUpdate = None

	def _localPositionChangeEvent(self, handle, userPtr, position):
		if self._PositionChange == None:
			return
		self._PositionChange(self, position)

	def setOnPositionChangeHandler(self, handler):
		if handler == None:
			self._PositionChange = None
			self._onPositionChange = None
		else:
			self._PositionChange = handler
			self._onPositionChange = self._PositionChangeFactory(self._localPositionChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def getAcceleration(self):
		_Acceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Acceleration))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Acceleration.value

	def setAcceleration(self, Acceleration):
		_Acceleration = ctypes.c_double(Acceleration)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Acceleration)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinAcceleration(self):
		_MinAcceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinAcceleration))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinAcceleration.value

	def getMaxAcceleration(self):
		_MaxAcceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxAcceleration))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxAcceleration.value

	def getCurrentLimit(self):
		_CurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_CurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _CurrentLimit.value

	def setCurrentLimit(self, CurrentLimit):
		_CurrentLimit = ctypes.c_double(CurrentLimit)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _CurrentLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinCurrentLimit(self):
		_MinCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinCurrentLimit.value

	def getMaxCurrentLimit(self):
		_MaxCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxCurrentLimit.value

	def getCurrentRegulatorGain(self):
		_CurrentRegulatorGain = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getCurrentRegulatorGain
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_CurrentRegulatorGain))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _CurrentRegulatorGain.value

	def setCurrentRegulatorGain(self, CurrentRegulatorGain):
		_CurrentRegulatorGain = ctypes.c_double(CurrentRegulatorGain)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setCurrentRegulatorGain
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _CurrentRegulatorGain)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinCurrentRegulatorGain(self):
		_MinCurrentRegulatorGain = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinCurrentRegulatorGain
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinCurrentRegulatorGain))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinCurrentRegulatorGain.value

	def getMaxCurrentRegulatorGain(self):
		_MaxCurrentRegulatorGain = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxCurrentRegulatorGain
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxCurrentRegulatorGain))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxCurrentRegulatorGain.value

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getDeadBand(self):
		_DeadBand = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getDeadBand
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_DeadBand))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _DeadBand.value

	def setDeadBand(self, DeadBand):
		_DeadBand = ctypes.c_double(DeadBand)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setDeadBand
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DeadBand)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getDutyCycle(self):
		_DutyCycle = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getDutyCycle
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_DutyCycle))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _DutyCycle.value

	def getEngaged(self):
		_Engaged = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getEngaged
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Engaged))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Engaged.value

	def setEngaged(self, Engaged):
		_Engaged = ctypes.c_int(Engaged)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setEngaged
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Engaged)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getFanMode(self):
		_FanMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getFanMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_FanMode))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _FanMode.value

	def setFanMode(self, FanMode):
		_FanMode = ctypes.c_int(FanMode)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setFanMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _FanMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getIOMode(self):
		_IOMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getIOMode
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
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setIOMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _IOMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getKd(self):
		_Kd = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getKd
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Kd))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Kd.value

	def setKd(self, Kd):
		_Kd = ctypes.c_double(Kd)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setKd
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Kd)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getKp(self):
		_Kp = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getKp
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Kp))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Kp.value

	def setKp(self, Kp):
		_Kp = ctypes.c_double(Kp)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setKp
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Kp)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getPosition(self):
		_Position = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Position))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Position.value

	def getMinPosition(self):
		_MinPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPosition))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPosition.value

	def getMaxPosition(self):
		_MaxPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPosition))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPosition.value

	def addPositionOffset(self, positionOffset):
		_positionOffset = ctypes.c_double(positionOffset)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_addPositionOffset
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _positionOffset)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getRescaleFactor(self):
		_RescaleFactor = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getRescaleFactor
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_RescaleFactor))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _RescaleFactor.value

	def setRescaleFactor(self, RescaleFactor):
		_RescaleFactor = ctypes.c_double(RescaleFactor)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setRescaleFactor
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _RescaleFactor)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getStallVelocity(self):
		_StallVelocity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getStallVelocity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_StallVelocity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _StallVelocity.value

	def setStallVelocity(self, StallVelocity):
		_StallVelocity = ctypes.c_double(StallVelocity)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setStallVelocity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _StallVelocity)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinStallVelocity(self):
		_MinStallVelocity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinStallVelocity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinStallVelocity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinStallVelocity.value

	def getMaxStallVelocity(self):
		_MaxStallVelocity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxStallVelocity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxStallVelocity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxStallVelocity.value

	def getTargetPosition(self):
		_TargetPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getTargetPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_TargetPosition))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _TargetPosition.value

	def setTargetPosition(self, TargetPosition):
		_TargetPosition = ctypes.c_double(TargetPosition)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setTargetPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _TargetPosition)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localsetTargetPosition_async(self, handle, ctx, res):

		if self._setTargetPosition_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._setTargetPosition_async(self, res, details)

	def setTargetPosition_async(self, TargetPosition, asyncHandler, ctx, fptr):
		if fptr == None:
			self._setTargetPosition_async = None
			self._onsetTargetPosition_async = None
		else:
			self._setTargetPosition_async = fptr
			self._onsetTargetPosition_async = self._asyncFactory(self._localsetTargetPosition_async)

		_TargetPosition = ctypes.c_double(TargetPosition)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setTargetPosition_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsetTargetPosition_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getVelocityLimit(self):
		_VelocityLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_VelocityLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _VelocityLimit.value

	def setVelocityLimit(self, VelocityLimit):
		_VelocityLimit = ctypes.c_double(VelocityLimit)

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_setVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _VelocityLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinVelocityLimit(self):
		_MinVelocityLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMinVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinVelocityLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinVelocityLimit.value

	def getMaxVelocityLimit(self):
		_MaxVelocityLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetMotorPositionController_getMaxVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxVelocityLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxVelocityLimit.value
