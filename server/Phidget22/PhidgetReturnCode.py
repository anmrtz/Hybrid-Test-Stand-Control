import sys
import ctypes
class PhidgetReturnCode:
	# Success
	EPHIDGET_OK = 0
	# Not Permitted
	EPHIDGET_PERM = 1
	# No Such Entity
	EPHIDGET_NOENT = 2
	# Timed Out
	EPHIDGET_TIMEOUT = 3
	# Keep Alive Failure
	EPHIDGET_KEEPALIVE = 58
	# Op Interrupted
	EPHIDGET_INTERRUPTED = 4
	# IO Issue
	EPHIDGET_IO = 5
	# Memory Issue
	EPHIDGET_NOMEMORY = 6
	# Access (Permission) Issue
	EPHIDGET_ACCESS = 7
	# Address Issue
	EPHIDGET_FAULT = 8
	# Resource Busy
	EPHIDGET_BUSY = 9
	# Object Exists
	EPHIDGET_EXIST = 10
	# Object is not a directory
	EPHIDGET_NOTDIR = 11
	# Object is a directory
	EPHIDGET_ISDIR = 12
	# Invalid
	EPHIDGET_INVALID = 13
	# Too many open files in system
	EPHIDGET_NFILE = 14
	# Too many open files
	EPHIDGET_MFILE = 15
	# Not enough space
	EPHIDGET_NOSPC = 16
	# File too Big
	EPHIDGET_FBIG = 17
	# Read Only Filesystem
	EPHIDGET_ROFS = 18
	# Read Only Object
	EPHIDGET_RO = 19
	# Operation Not Supported
	EPHIDGET_UNSUPPORTED = 20
	# Invalid Argument
	EPHIDGET_INVALIDARG = 21
	# Try again
	EPHIDGET_AGAIN = 22
	# End of File
	EPHIDGET_EOF = 31
	# Unexpected Error
	EPHIDGET_UNEXPECTED = 28
	# Duplicate
	EPHIDGET_DUPLICATE = 27
	# Bad Credential
	EPHIDGET_BADPASSWORD = 37
	# Network Unavailable
	EPHIDGET_NETUNAVAIL = 45
	# Connection Refused
	EPHIDGET_CONNREF = 35
	# Connection Reset
	EPHIDGET_CONNRESET = 46
	# No route to host
	EPHIDGET_HOSTUNREACH = 48
	# No Such Device
	EPHIDGET_NODEV = 40
	# Wrong Device
	EPHIDGET_WRONGDEVICE = 50
	# Broken Pipe
	EPHIDGET_PIPE = 41
	# Name Resolution Failure
	EPHIDGET_RESOLV = 44
	# Unknown or Invalid Value
	EPHIDGET_UNKNOWNVAL = 51
	# Device not Attached
	EPHIDGET_NOTATTACHED = 52
	# Invalid or Unexpected Packet
	EPHIDGET_INVALIDPACKET = 53
	# Argument List Too Long
	EPHIDGET_2BIG = 54
	# Bad Version
	EPHIDGET_BADVERSION = 55
	# Closed
	EPHIDGET_CLOSED = 56
	# Not Configured
	EPHIDGET_NOTCONFIGURED = 57

	@classmethod
	def getName(self, val):
		if val == self.EPHIDGET_OK:
			return "EPHIDGET_OK"
		if val == self.EPHIDGET_PERM:
			return "EPHIDGET_PERM"
		if val == self.EPHIDGET_NOENT:
			return "EPHIDGET_NOENT"
		if val == self.EPHIDGET_TIMEOUT:
			return "EPHIDGET_TIMEOUT"
		if val == self.EPHIDGET_KEEPALIVE:
			return "EPHIDGET_KEEPALIVE"
		if val == self.EPHIDGET_INTERRUPTED:
			return "EPHIDGET_INTERRUPTED"
		if val == self.EPHIDGET_IO:
			return "EPHIDGET_IO"
		if val == self.EPHIDGET_NOMEMORY:
			return "EPHIDGET_NOMEMORY"
		if val == self.EPHIDGET_ACCESS:
			return "EPHIDGET_ACCESS"
		if val == self.EPHIDGET_FAULT:
			return "EPHIDGET_FAULT"
		if val == self.EPHIDGET_BUSY:
			return "EPHIDGET_BUSY"
		if val == self.EPHIDGET_EXIST:
			return "EPHIDGET_EXIST"
		if val == self.EPHIDGET_NOTDIR:
			return "EPHIDGET_NOTDIR"
		if val == self.EPHIDGET_ISDIR:
			return "EPHIDGET_ISDIR"
		if val == self.EPHIDGET_INVALID:
			return "EPHIDGET_INVALID"
		if val == self.EPHIDGET_NFILE:
			return "EPHIDGET_NFILE"
		if val == self.EPHIDGET_MFILE:
			return "EPHIDGET_MFILE"
		if val == self.EPHIDGET_NOSPC:
			return "EPHIDGET_NOSPC"
		if val == self.EPHIDGET_FBIG:
			return "EPHIDGET_FBIG"
		if val == self.EPHIDGET_ROFS:
			return "EPHIDGET_ROFS"
		if val == self.EPHIDGET_RO:
			return "EPHIDGET_RO"
		if val == self.EPHIDGET_UNSUPPORTED:
			return "EPHIDGET_UNSUPPORTED"
		if val == self.EPHIDGET_INVALIDARG:
			return "EPHIDGET_INVALIDARG"
		if val == self.EPHIDGET_AGAIN:
			return "EPHIDGET_AGAIN"
		if val == self.EPHIDGET_EOF:
			return "EPHIDGET_EOF"
		if val == self.EPHIDGET_UNEXPECTED:
			return "EPHIDGET_UNEXPECTED"
		if val == self.EPHIDGET_DUPLICATE:
			return "EPHIDGET_DUPLICATE"
		if val == self.EPHIDGET_BADPASSWORD:
			return "EPHIDGET_BADPASSWORD"
		if val == self.EPHIDGET_NETUNAVAIL:
			return "EPHIDGET_NETUNAVAIL"
		if val == self.EPHIDGET_CONNREF:
			return "EPHIDGET_CONNREF"
		if val == self.EPHIDGET_CONNRESET:
			return "EPHIDGET_CONNRESET"
		if val == self.EPHIDGET_HOSTUNREACH:
			return "EPHIDGET_HOSTUNREACH"
		if val == self.EPHIDGET_NODEV:
			return "EPHIDGET_NODEV"
		if val == self.EPHIDGET_WRONGDEVICE:
			return "EPHIDGET_WRONGDEVICE"
		if val == self.EPHIDGET_PIPE:
			return "EPHIDGET_PIPE"
		if val == self.EPHIDGET_RESOLV:
			return "EPHIDGET_RESOLV"
		if val == self.EPHIDGET_UNKNOWNVAL:
			return "EPHIDGET_UNKNOWNVAL"
		if val == self.EPHIDGET_NOTATTACHED:
			return "EPHIDGET_NOTATTACHED"
		if val == self.EPHIDGET_INVALIDPACKET:
			return "EPHIDGET_INVALIDPACKET"
		if val == self.EPHIDGET_2BIG:
			return "EPHIDGET_2BIG"
		if val == self.EPHIDGET_BADVERSION:
			return "EPHIDGET_BADVERSION"
		if val == self.EPHIDGET_CLOSED:
			return "EPHIDGET_CLOSED"
		if val == self.EPHIDGET_NOTCONFIGURED:
			return "EPHIDGET_NOTCONFIGURED"
		return "<invalid enumeration value>"
