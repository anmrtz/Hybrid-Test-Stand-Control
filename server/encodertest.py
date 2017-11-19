import sys
import time
from Phidget22.Devices.Encoder import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

try:
	ch = Encoder()
except RuntimeError as e:
	print("Runtime Exception %s" % e.details)
	print("Press Enter to Exit...\n")
	readin = sys.stdin.read(1)
	exit(1)

def EncoderAttached(e):
	try:
		attached = e
		print("\nAttach Event Detected (Information Below)")
		print("===========================================")
		print("Library Version: %s" % attached.getLibraryVersion())
		print("Serial Number: %d" % attached.getDeviceSerialNumber())
		print("Channel: %d" % attached.getChannel())
		print("Channel Class: %s" % attached.getChannelClass())
		print("Channel Name: %s" % attached.getChannelName())
		print("Device ID: %d" % attached.getDeviceID())
		print("Device Version: %d" % attached.getDeviceVersion())
		print("Device Name: %s" % attached.getDeviceName())
		print("Device Class: %d" % attached.getDeviceClass())
		print("\n")

	except PhidgetException as e:
		print("Phidget Exception %i: %s" % (e.code, e.details))
		print("Press Enter to Exit...\n")
		readin = sys.stdin.read(1)
		exit(1)

def EncoderDetached(e):
	detached = e
	try:
		print("\nDetach event on Port %d Channel %d" % (detached.getHubPort(), detached.getChannel()))
	except PhidgetException as e:
		print("Phidget Exception %i: %s" % (e.code, e.details))
		print("Press Enter to Exit...\n")
		readin = sys.stdin.read(1)
		exit(1)

def ErrorEvent(e, eCode, description):
	print("Error %i : %s" % (eCode, description))

def PositionChangeHandler(e, positionChange, timeChange, indexTriggered):
	curr_pos = ch.getPosition() 
	print("Position Changed: %7d %7d  %7.3lf  %d\n" % (curr_pos, positionChange, timeChange, indexTriggered))

try:
	ch.setOnAttachHandler(EncoderAttached)
	ch.setOnDetachHandler(EncoderDetached)
	ch.setOnErrorHandler(ErrorEvent)

	ch.setOnPositionChangeHandler(PositionChangeHandler)

	# Please review the Phidget22 channel matching documentation for details on the device
	# and class architecture of Phidget22, and how channels are matched to device features.

	# Specifies the serial number of the device to attach to.
	# For VINT devices, this is the hub serial number.
	#
	# The default is any device.
	#
	# ch.setDeviceSerialNumber(<YOUR DEVICE SERIAL NUMBER>)

	# For VINT devices, this specifies the port the VINT device must be plugged into.
	#
	# The default is any port.
	#
	# ch.setHubPort(0)

	# Specifies which channel to attach to.  It is important that the channel of
	# the device is the same class as the channel that is being opened.
	#
	# The default is any channel.
	#
	# ch.setChannel(0)

	# In order to attach to a network Phidget, the program must connect to a Phidget22 Network Server.
	# In a normal environment this can be done automatically by enabling server discovery, which
	# will cause the client to discovery and connect to available servers.
	#
	# To force the channel to only match a network Phidget, set remote to 1.
	#
	# Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICE);
	# ch.setIsRemote(1)

	print("Waiting for the Phidget Encoder Object to be attached...")
	ch.openWaitForAttachment(5000)
	ch.setDataInterval(10)
	ch.setPosition(0)
except PhidgetException as e:
	print("Phidget Exception %i: %s" % (e.code, e.details))
	print("Press Enter to Exit...\n")
	readin = sys.stdin.read(1)
	exit(1)

if(not ch.getEnabled()):
	ch.setEnabled(1)

print("Gathering data for 10 seconds...")
time.sleep(20)

try:
	ch.close()
except PhidgetException as e:
	print("Phidget Exception %i: %s" % (e.code, e.details))
	print("Press Enter to Exit...\n")
	readin = sys.stdin.read(1)
	exit(1)
print("Closed Encoder device")
exit(0)

