import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.RCServoVoltage import RCServoVoltage
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class RCServo(Phidget):

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
			self._PositionChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._PositionChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._PositionChange = None
		self._onPositionChange = None

		if sys.platform == 'win32':
			self._TargetPositionReachedFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._TargetPositionReachedFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._TargetPositionReached = None
		self._onTargetPositionReached = None

		if sys.platform == 'win32':
			self._VelocityChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._VelocityChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._VelocityChange = None
		self._onVelocityChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

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
			__func = PhidgetSupport.getDll().PhidgetRCServo_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def _localTargetPositionReachedEvent(self, handle, userPtr, position):
		if self._TargetPositionReached == None:
			return
		self._TargetPositionReached(self, position)

	def setOnTargetPositionReachedHandler(self, handler):
		if handler == None:
			self._TargetPositionReached = None
			self._onTargetPositionReached = None
		else:
			self._TargetPositionReached = handler
			self._onTargetPositionReached = self._TargetPositionReachedFactory(self._localTargetPositionReachedEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setOnTargetPositionReachedHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onTargetPositionReached, None)
		except RuntimeError:
			self._TargetPositionReached = None
			self._onTargetPositionReached = None

	def _localVelocityChangeEvent(self, handle, userPtr, velocity):
		if self._VelocityChange == None:
			return
		self._VelocityChange(self, velocity)

	def setOnVelocityChangeHandler(self, handler):
		if handler == None:
			self._VelocityChange = None
			self._onVelocityChange = None
		else:
			self._VelocityChange = handler
			self._onVelocityChange = self._VelocityChangeFactory(self._localVelocityChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setOnVelocityChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onVelocityChange, None)
		except RuntimeError:
			self._VelocityChange = None
			self._onVelocityChange = None

	def getAcceleration(self):
		_Acceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getAcceleration
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_setAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Acceleration)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinAcceleration(self):
		_MinAcceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinAcceleration
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxAcceleration))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxAcceleration.value

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxDataInterval))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxDataInterval.value

	def getEngaged(self):
		_Engaged = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getEngaged
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_setEngaged
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Engaged)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getIsMoving(self):
		_IsMoving = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getIsMoving
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_IsMoving))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _IsMoving.value

	def getPosition(self):
		_Position = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Position))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Position.value

	def setMinPosition(self, MinPosition):
		_MinPosition = ctypes.c_double(MinPosition)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setMinPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _MinPosition)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinPosition(self):
		_MinPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPosition))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPosition.value

	def setMaxPosition(self, MaxPosition):
		_MaxPosition = ctypes.c_double(MaxPosition)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setMaxPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _MaxPosition)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMaxPosition(self):
		_MaxPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxPosition
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPosition))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPosition.value

	def setMinPulseWidth(self, MinPulseWidth):
		_MinPulseWidth = ctypes.c_double(MinPulseWidth)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setMinPulseWidth
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _MinPulseWidth)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinPulseWidth(self):
		_MinPulseWidth = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinPulseWidth
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPulseWidth))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPulseWidth.value

	def setMaxPulseWidth(self, MaxPulseWidth):
		_MaxPulseWidth = ctypes.c_double(MaxPulseWidth)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setMaxPulseWidth
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _MaxPulseWidth)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMaxPulseWidth(self):
		_MaxPulseWidth = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxPulseWidth
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPulseWidth))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPulseWidth.value

	def getMinPulseWidthLimit(self):
		_MinPulseWidthLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinPulseWidthLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinPulseWidthLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinPulseWidthLimit.value

	def getMaxPulseWidthLimit(self):
		_MaxPulseWidthLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxPulseWidthLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxPulseWidthLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxPulseWidthLimit.value

	def getSpeedRampingState(self):
		_SpeedRampingState = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getSpeedRampingState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_SpeedRampingState))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _SpeedRampingState.value

	def setSpeedRampingState(self, SpeedRampingState):
		_SpeedRampingState = ctypes.c_int(SpeedRampingState)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setSpeedRampingState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _SpeedRampingState)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getTargetPosition(self):
		_TargetPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getTargetPosition
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_setTargetPosition
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

	def getTorque(self):
		_Torque = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getTorque
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Torque))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Torque.value

	def setTorque(self, Torque):
		_Torque = ctypes.c_double(Torque)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setTorque
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Torque)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinTorque(self):
		_MinTorque = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinTorque
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinTorque))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinTorque.value

	def getMaxTorque(self):
		_MaxTorque = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxTorque
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxTorque))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxTorque.value

	def getVelocity(self):
		_Velocity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getVelocity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Velocity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Velocity.value

	def getVelocityLimit(self):
		_VelocityLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getVelocityLimit
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_setVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _VelocityLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinVelocityLimit(self):
		_MinVelocityLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMinVelocityLimit
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
			__func = PhidgetSupport.getDll().PhidgetRCServo_getMaxVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxVelocityLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxVelocityLimit.value

	def getVoltage(self):
		_Voltage = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_getVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Voltage))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Voltage.value

	def setVoltage(self, Voltage):
		_Voltage = ctypes.c_int(Voltage)

		try:
			__func = PhidgetSupport.getDll().PhidgetRCServo_setVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Voltage)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

