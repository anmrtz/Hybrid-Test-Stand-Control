import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.FanMode import FanMode
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class PowerGuard(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def getFanMode(self):
		_FanMode = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_getFanMode
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
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_setFanMode
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _FanMode)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getOverVoltage(self):
		_OverVoltage = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_getOverVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_OverVoltage))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _OverVoltage.value

	def setOverVoltage(self, OverVoltage):
		_OverVoltage = ctypes.c_double(OverVoltage)

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_setOverVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _OverVoltage)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinOverVoltage(self):
		_MinOverVoltage = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_getMinOverVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinOverVoltage))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinOverVoltage.value

	def getMaxOverVoltage(self):
		_MaxOverVoltage = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_getMaxOverVoltage
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxOverVoltage))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxOverVoltage.value

	def getPowerEnabled(self):
		_PowerEnabled = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_getPowerEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_PowerEnabled))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _PowerEnabled.value

	def setPowerEnabled(self, PowerEnabled):
		_PowerEnabled = ctypes.c_int(PowerEnabled)

		try:
			__func = PhidgetSupport.getDll().PhidgetPowerGuard_setPowerEnabled
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _PowerEnabled)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

