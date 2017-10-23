import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.ControlMode import ControlMode
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class Stepper(Phidget):

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
			self._StoppedFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
		else:
			self._StoppedFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p)
		self._Stopped = None
		self._onStopped = None

		if sys.platform == 'win32':
			self._VelocityChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		else:
			self._VelocityChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double)
		self._VelocityChange = None
		self._onVelocityChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_create
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def _localStoppedEvent(self, handle, userPtr):
		if self._Stopped == None:
			return
		self._Stopped(self)

	def setOnStoppedHandler(self, handler):
		if handler == None:
			self._Stopped = None
			self._onStopped = None
		else:
			self._Stopped = handler
			self._onStopped = self._StoppedFactory(self._localStoppedEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_setOnStoppedHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onStopped, None)
		except RuntimeError:
			self._Stopped = None
			self._onStopped = None

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
			__func = PhidgetSupport.getDll().PhidgetStepper_setOnVelocityChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onVelocityChange, None)
		except RuntimeError:
			self._VelocityChange = None
			self._onVelocityChange = None

	def getAcceleration(self):
		_Acceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getAcceleration
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Acceleration)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinAcceleration(self):
		_MinAcceleration = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getMinAcceleration
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getMaxAcceleration
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxAcceleration))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxAcceleration.value

	def getControlMode(self):
		_ControlMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getControlMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_ControlMode))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _ControlMode.value

	def setControlMode(self, ControlMode):
		_ControlMode = ctypes.c_int(ControlMode)

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_setControlMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _ControlMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getCurrentLimit(self):
		_CurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getCurrentLimit
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _CurrentLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinCurrentLimit(self):
		_MinCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getMinCurrentLimit
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getMaxCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxCurrentLimit.value

	def getDataInterval(self):
		_DataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setDataInterval
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _DataInterval)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinDataInterval(self):
		_MinDataInterval = ctypes.c_uint32()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getMinDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getMaxDataInterval
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getEngaged
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setEngaged
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Engaged)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getHoldingCurrentLimit(self):
		_HoldingCurrentLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getHoldingCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_HoldingCurrentLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _HoldingCurrentLimit.value

	def setHoldingCurrentLimit(self, HoldingCurrentLimit):
		_HoldingCurrentLimit = ctypes.c_double(HoldingCurrentLimit)

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_setHoldingCurrentLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _HoldingCurrentLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getIsMoving(self):
		_IsMoving = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getIsMoving
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getPosition
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getMinPosition
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getMaxPosition
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
			__func = PhidgetSupport.getDll().PhidgetStepper_addPositionOffset
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _positionOffset)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getRescaleFactor(self):
		_RescaleFactor = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getRescaleFactor
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setRescaleFactor
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _RescaleFactor)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getTargetPosition(self):
		_TargetPosition = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getTargetPosition
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setTargetPosition
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

	def getVelocity(self):
		_Velocity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getVelocity
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getVelocityLimit
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
			__func = PhidgetSupport.getDll().PhidgetStepper_setVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _VelocityLimit)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinVelocityLimit(self):
		_MinVelocityLimit = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetStepper_getMinVelocityLimit
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
			__func = PhidgetSupport.getDll().PhidgetStepper_getMaxVelocityLimit
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxVelocityLimit))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxVelocityLimit.value
