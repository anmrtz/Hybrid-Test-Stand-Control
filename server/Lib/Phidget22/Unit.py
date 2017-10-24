import sys
import ctypes
class Unit:
	# Unitless
	PHIDUNIT_NONE = 0
	# Boolean
	PHIDUNIT_BOOLEAN = 1
	# Percent
	PHIDUNIT_PERCENT = 2
	# Decibel
	PHIDUNIT_DECIBEL = 3
	# Millimeter
	PHIDUNIT_MILLIMETER = 4
	# Centimeter
	PHIDUNIT_CENTIMETER = 5
	# Meter
	PHIDUNIT_METER = 6
	# Gram
	PHIDUNIT_GRAM = 7
	# Kilogram
	PHIDUNIT_KILOGRAM = 8
	# Milliampere
	PHIDUNIT_MILLIAMPERE = 9
	# Ampere
	PHIDUNIT_AMPERE = 10
	# Kilopascal
	PHIDUNIT_KILOPASCAL = 11
	# Volt
	PHIDUNIT_VOLT = 12
	# Degree Celcius
	PHIDUNIT_DEGREE_CELCIUS = 13
	# Lux
	PHIDUNIT_LUX = 14
	# Gauss
	PHIDUNIT_GAUSS = 15
	# pH
	PHIDUNIT_PH = 16
	# Watt
	PHIDUNIT_WATT = 17

	@classmethod
	def getName(self, val):
		if val == self.PHIDUNIT_NONE:
			return "PHIDUNIT_NONE"
		if val == self.PHIDUNIT_BOOLEAN:
			return "PHIDUNIT_BOOLEAN"
		if val == self.PHIDUNIT_PERCENT:
			return "PHIDUNIT_PERCENT"
		if val == self.PHIDUNIT_DECIBEL:
			return "PHIDUNIT_DECIBEL"
		if val == self.PHIDUNIT_MILLIMETER:
			return "PHIDUNIT_MILLIMETER"
		if val == self.PHIDUNIT_CENTIMETER:
			return "PHIDUNIT_CENTIMETER"
		if val == self.PHIDUNIT_METER:
			return "PHIDUNIT_METER"
		if val == self.PHIDUNIT_GRAM:
			return "PHIDUNIT_GRAM"
		if val == self.PHIDUNIT_KILOGRAM:
			return "PHIDUNIT_KILOGRAM"
		if val == self.PHIDUNIT_MILLIAMPERE:
			return "PHIDUNIT_MILLIAMPERE"
		if val == self.PHIDUNIT_AMPERE:
			return "PHIDUNIT_AMPERE"
		if val == self.PHIDUNIT_KILOPASCAL:
			return "PHIDUNIT_KILOPASCAL"
		if val == self.PHIDUNIT_VOLT:
			return "PHIDUNIT_VOLT"
		if val == self.PHIDUNIT_DEGREE_CELCIUS:
			return "PHIDUNIT_DEGREE_CELCIUS"
		if val == self.PHIDUNIT_LUX:
			return "PHIDUNIT_LUX"
		if val == self.PHIDUNIT_GAUSS:
			return "PHIDUNIT_GAUSS"
		if val == self.PHIDUNIT_PH:
			return "PHIDUNIT_PH"
		if val == self.PHIDUNIT_WATT:
			return "PHIDUNIT_WATT"
		return "<invalid enumeration value>"
