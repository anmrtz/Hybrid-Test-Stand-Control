import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.GPSDate import GPSDate
from Phidget22.GPSTime import GPSTime
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class GPS(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._HeadingChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
		else:
			self._HeadingChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double)
		self._HeadingChange = None
		self._onHeadingChange = None

		if sys.platform == 'win32':
			self._PositionChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double)
		else:
			self._PositionChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_double, ctypes.c_double, ctypes.c_double)
		self._PositionChange = None
		self._onPositionChange = None

		if sys.platform == 'win32':
			self._PositionFixStateChangeFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		else:
			self._PositionFixStateChangeFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		self._PositionFixStateChange = None
		self._onPositionFixStateChange = None

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def _localHeadingChangeEvent(self, handle, userPtr, heading, velocity):
		if self._HeadingChange == None:
			return
		self._HeadingChange(self, heading, velocity)

	def setOnHeadingChangeHandler(self, handler):
		if handler == None:
			self._HeadingChange = None
			self._onHeadingChange = None
		else:
			self._HeadingChange = handler
			self._onHeadingChange = self._HeadingChangeFactory(self._localHeadingChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_setOnHeadingChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onHeadingChange, None)
		except RuntimeError:
			self._HeadingChange = None
			self._onHeadingChange = None

	def _localPositionChangeEvent(self, handle, userPtr, latitude, longitude, altitude):
		if self._PositionChange == None:
			return
		self._PositionChange(self, latitude, longitude, altitude)

	def setOnPositionChangeHandler(self, handler):
		if handler == None:
			self._PositionChange = None
			self._onPositionChange = None
		else:
			self._PositionChange = handler
			self._onPositionChange = self._PositionChangeFactory(self._localPositionChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_setOnPositionChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionChange, None)
		except RuntimeError:
			self._PositionChange = None
			self._onPositionChange = None

	def _localPositionFixStateChangeEvent(self, handle, userPtr, positionFixState):
		if self._PositionFixStateChange == None:
			return
		self._PositionFixStateChange(self, positionFixState)

	def setOnPositionFixStateChangeHandler(self, handler):
		if handler == None:
			self._PositionFixStateChange = None
			self._onPositionFixStateChange = None
		else:
			self._PositionFixStateChange = handler
			self._onPositionFixStateChange = self._PositionFixStateChangeFactory(self._localPositionFixStateChangeEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_setOnPositionFixStateChangeHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onPositionFixStateChange, None)
		except RuntimeError:
			self._PositionFixStateChange = None
			self._onPositionFixStateChange = None

	def getAltitude(self):
		_Altitude = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getAltitude
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Altitude))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Altitude.value

	def getDate(self):
		_Date = GPSDate()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getDate
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Date))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Date.toPython()

	def getHeading(self):
		_Heading = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getHeading
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Heading))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Heading.value

	def getLatitude(self):
		_Latitude = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getLatitude
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Latitude))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Latitude.value

	def getLongitude(self):
		_Longitude = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getLongitude
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Longitude))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Longitude.value

	def getPositionFixState(self):
		_PositionFixState = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getPositionFixState
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PositionFixState))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PositionFixState.value

	def getTime(self):
		_Time = GPSTime()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getTime
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Time))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Time.toPython()

	def getVelocity(self):
		_Velocity = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetGPS_getVelocity
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Velocity))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Velocity.value
