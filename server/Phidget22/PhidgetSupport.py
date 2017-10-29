import threading
import sys
import ctypes
from ctypes import *

class PhidgetSupport:
	__dll = None

	@staticmethod
	def getDll():
		if PhidgetSupport.__dll is None:
			if sys.platform == 'win32':
				PhidgetSupport.__dll = windll.LoadLibrary("phidget22.dll")
			elif sys.platform == 'darwin':
				PhidgetSupport.__dll = cdll.LoadLibrary("/Library/Frameworks/Phidget22.framework/Versions/Current/Phidget22")
			else:
				PhidgetSupport.__dll = cdll.LoadLibrary("libphidget22.so.0.0.0")
		return PhidgetSupport.__dll
					
	def __init__(self):
		self.handle = None

	def __del__(self):
		pass

	@staticmethod
	def versionChecked_ord(character):
		if(sys.version_info[0] < 3):
			return character
		else:
			return ord(character)
