import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.PhidgetServerType import PhidgetServerType
from Phidget22.PhidgetServer import PhidgetServer
from Phidget22.PhidgetServerType import PhidgetServerType
from Phidget22.PhidgetException import PhidgetException

class Net:

	def __init__(self):
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._ServerAddedFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(PhidgetServer), undefined)
		else:
			self._ServerAddedFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(PhidgetServer), undefined)
		self._ServerAdded = None
		self._onServerAdded = None

		if sys.platform == 'win32':
			self._ServerRemovedFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(PhidgetServer))
		else:
			self._ServerRemovedFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.POINTER(PhidgetServer))
		self._ServerRemoved = None
		self._onServerRemoved = None


	def __del__(self):
			pass

	def _localServerAddedEvent(self, userPtr, server, kv):
		if self._ServerAdded == None:
			return
		if server != None:
			server = server.contents
			server.toPython()
		self._ServerAdded(self, server, kv)

	def setOnServerAddedHandler(self, handler):
		if handler == None:
			self._ServerAdded = None
			self._onServerAdded = None
		else:
			self._ServerAdded = handler
			self._onServerAdded = self._ServerAddedFactory(self._localServerAddedEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_setOnServerAddedHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onServerAdded, None)
		except RuntimeError:
			self._ServerAdded = None
			self._onServerAdded = None

	def _localServerRemovedEvent(self, userPtr, server):
		if self._ServerRemoved == None:
			return
		if server != None:
			server = server.contents
			server.toPython()
		self._ServerRemoved(self, server)

	def setOnServerRemovedHandler(self, handler):
		if handler == None:
			self._ServerRemoved = None
			self._onServerRemoved = None
		else:
			self._ServerRemoved = handler
			self._onServerRemoved = self._ServerRemovedFactory(self._localServerRemovedEvent)

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_setOnServerRemovedHandler
			__func.restype = ctypes.c_int32
			res = __func(self.handle, self._onServerRemoved, None)
		except RuntimeError:
			self._ServerRemoved = None
			self._onServerRemoved = None

	@staticmethod
	def addServer(srvname, address, port, passwd, flags):
		_srvname = ctypes.create_string_buffer(srvname.encode('utf-8'))
		_address = ctypes.create_string_buffer(address.encode('utf-8'))
		_port = ctypes.c_int(port)
		_passwd = ctypes.create_string_buffer(passwd.encode('utf-8'))
		_flags = ctypes.c_int(flags)

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_addServer
			__func.restype = ctypes.c_int32
			result = __func(ctypes.byref(_srvname), ctypes.byref(_address), _port, ctypes.byref(_passwd), _flags)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	@staticmethod
	def removeServer(srvname):
		_srvname = ctypes.create_string_buffer(srvname.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_removeServer
			__func.restype = ctypes.c_int32
			result = __func(ctypes.byref(_srvname))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	@staticmethod
	def enableServer(srvname):
		_srvname = ctypes.create_string_buffer(srvname.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_enableServer
			__func.restype = ctypes.c_int32
			result = __func(ctypes.byref(_srvname))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	@staticmethod
	def disableServer(srvname, flags):
		_srvname = ctypes.create_string_buffer(srvname.encode('utf-8'))
		_flags = ctypes.c_int(flags)

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_disableServer
			__func.restype = ctypes.c_int32
			result = __func(ctypes.byref(_srvname), _flags)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	@staticmethod
	def enableServerDiscovery(serverType):
		_serverType = ctypes.c_int(serverType)

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_enableServerDiscovery
			__func.restype = ctypes.c_int32
			result = __func(_serverType)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	@staticmethod
	def disableServerDiscovery(serverType):
		_serverType = ctypes.c_int(serverType)

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_disableServerDiscovery
			__func.restype = ctypes.c_int32
			result = __func(_serverType)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	@staticmethod
	def setServerPassword(srvname, passwd):
		_srvname = ctypes.create_string_buffer(srvname.encode('utf-8'))
		_passwd = ctypes.create_string_buffer(passwd.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetNet_setServerPassword
			__func.restype = ctypes.c_int32
			result = __func(ctypes.byref(_srvname), ctypes.byref(_passwd))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

