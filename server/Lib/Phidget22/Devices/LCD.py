import sys
import ctypes
from Phidget22.PhidgetSupport import PhidgetSupport
from Phidget22.LCDFont import LCDFont
from Phidget22.LCDPixelState import LCDPixelState
from Phidget22.LCDScreenSize import LCDScreenSize
from Phidget22.PhidgetException import PhidgetException

from Phidget22.Phidget import Phidget

class LCD(Phidget):

	def __init__(self):
		Phidget.__init__(self)
		self.handle = ctypes.c_void_p()

		if sys.platform == 'win32':
			self._asyncFactory = ctypes.WINFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)
		else:
			self._asyncFactory = ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int)

		self._setCharacterBitmap_async = None
		self._onsetCharacterBitmap_async = None
		self._clear_async = None
		self._onclear_async = None
		self._copy_async = None
		self._oncopy_async = None
		self._drawLine_async = None
		self._ondrawLine_async = None
		self._drawPixel_async = None
		self._ondrawPixel_async = None
		self._drawRect_async = None
		self._ondrawRect_async = None
		self._flush_async = None
		self._onflush_async = None
		self._setFrameBuffer_async = None
		self._onsetFrameBuffer_async = None
		self._saveFrameBuffer_async = None
		self._onsaveFrameBuffer_async = None
		self._writeBitmap_async = None
		self._onwriteBitmap_async = None
		self._writeText_async = None
		self._onwriteText_async = None

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_create
			__func.restype = ctypes.c_int32
			res = __func(ctypes.byref(self.handle))
		except RuntimeError:
			raise

		if res > 0:
			raise PhidgetException(res)

	def __del__(self):
		Phidget.__del__(self)

	def getBacklight(self):
		_Backlight = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getBacklight
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Backlight))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Backlight.value

	def setBacklight(self, Backlight):
		_Backlight = ctypes.c_double(Backlight)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setBacklight
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Backlight)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinBacklight(self):
		_MinBacklight = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getMinBacklight
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinBacklight))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinBacklight.value

	def getMaxBacklight(self):
		_MaxBacklight = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getMaxBacklight
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxBacklight))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxBacklight.value

	def setCharacterBitmap(self, font, character, bitmap):
		_font = ctypes.c_int(font)
		_character = ctypes.create_string_buffer(character.encode('utf-8'))
		_bitmap = (ctypes.c_uint8 * len(bitmap))(*bitmap)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setCharacterBitmap
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _font, ctypes.byref(_character), ctypes.byref(_bitmap))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localsetCharacterBitmap_async(self, handle, ctx, res):

		if self._setCharacterBitmap_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._setCharacterBitmap_async(self, res, details)

	def setCharacterBitmap_async(self, font, character, bitmap, asyncHandler, ctx, fptr):
		if fptr == None:
			self._setCharacterBitmap_async = None
			self._onsetCharacterBitmap_async = None
		else:
			self._setCharacterBitmap_async = fptr
			self._onsetCharacterBitmap_async = self._asyncFactory(self._localsetCharacterBitmap_async)

		_font = ctypes.c_int(font)
		_character = ctypes.create_string_buffer(character.encode('utf-8'))
		_bitmap = (ctypes.c_uint8 * len(bitmap))(*bitmap)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setCharacterBitmap_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsetCharacterBitmap_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getMaxCharacters(self, font):
		_font = ctypes.c_int(font)
		_maxCharacters = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getMaxCharacters
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _font, ctypes.byref(_maxCharacters))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _maxCharacters.value

	def clear(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_clear
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localclear_async(self, handle, ctx, res):

		if self._clear_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._clear_async(self, res, details)

	def clear_async(self, asyncHandler, ctx, fptr):
		if fptr == None:
			self._clear_async = None
			self._onclear_async = None
		else:
			self._clear_async = fptr
			self._onclear_async = self._asyncFactory(self._localclear_async)



		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_clear_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onclear_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getContrast(self):
		_Contrast = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getContrast
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Contrast))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Contrast.value

	def setContrast(self, Contrast):
		_Contrast = ctypes.c_double(Contrast)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setContrast
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Contrast)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getMinContrast(self):
		_MinContrast = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getMinContrast
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MinContrast))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MinContrast.value

	def getMaxContrast(self):
		_MaxContrast = ctypes.c_double()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getMaxContrast
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_MaxContrast))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _MaxContrast.value

	def copy(self, srcFramebuffer, dstFramebuffer, srcX1, srcY1, srcX2, srcY2, dstX, dstY, inverted):
		_srcFramebuffer = ctypes.c_int(srcFramebuffer)
		_dstFramebuffer = ctypes.c_int(dstFramebuffer)
		_srcX1 = ctypes.c_int(srcX1)
		_srcY1 = ctypes.c_int(srcY1)
		_srcX2 = ctypes.c_int(srcX2)
		_srcY2 = ctypes.c_int(srcY2)
		_dstX = ctypes.c_int(dstX)
		_dstY = ctypes.c_int(dstY)
		_inverted = ctypes.c_int(inverted)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_copy
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _srcFramebuffer, _dstFramebuffer, _srcX1, _srcY1, _srcX2, _srcY2, _dstX, _dstY, _inverted)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localcopy_async(self, handle, ctx, res):

		if self._copy_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._copy_async(self, res, details)

	def copy_async(self, srcFramebuffer, dstFramebuffer, srcX1, srcY1, srcX2, srcY2, dstX, dstY, inverted, asyncHandler, ctx, fptr):
		if fptr == None:
			self._copy_async = None
			self._oncopy_async = None
		else:
			self._copy_async = fptr
			self._oncopy_async = self._asyncFactory(self._localcopy_async)

		_srcFramebuffer = ctypes.c_int(srcFramebuffer)
		_dstFramebuffer = ctypes.c_int(dstFramebuffer)
		_srcX1 = ctypes.c_int(srcX1)
		_srcY1 = ctypes.c_int(srcY1)
		_srcX2 = ctypes.c_int(srcX2)
		_srcY2 = ctypes.c_int(srcY2)
		_dstX = ctypes.c_int(dstX)
		_dstY = ctypes.c_int(dstY)
		_inverted = ctypes.c_int(inverted)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_copy_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._oncopy_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getCursorBlink(self):
		_CursorBlink = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getCursorBlink
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_CursorBlink))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _CursorBlink.value

	def setCursorBlink(self, CursorBlink):
		_CursorBlink = ctypes.c_int(CursorBlink)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setCursorBlink
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _CursorBlink)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getCursorOn(self):
		_CursorOn = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getCursorOn
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_CursorOn))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _CursorOn.value

	def setCursorOn(self, CursorOn):
		_CursorOn = ctypes.c_int(CursorOn)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setCursorOn
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _CursorOn)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def drawLine(self, x1, y1, x2, y2):
		_x1 = ctypes.c_int(x1)
		_y1 = ctypes.c_int(y1)
		_x2 = ctypes.c_int(x2)
		_y2 = ctypes.c_int(y2)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_drawLine
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _x1, _y1, _x2, _y2)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localdrawLine_async(self, handle, ctx, res):

		if self._drawLine_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._drawLine_async(self, res, details)

	def drawLine_async(self, x1, y1, x2, y2, asyncHandler, ctx, fptr):
		if fptr == None:
			self._drawLine_async = None
			self._ondrawLine_async = None
		else:
			self._drawLine_async = fptr
			self._ondrawLine_async = self._asyncFactory(self._localdrawLine_async)

		_x1 = ctypes.c_int(x1)
		_y1 = ctypes.c_int(y1)
		_x2 = ctypes.c_int(x2)
		_y2 = ctypes.c_int(y2)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_drawLine_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._ondrawLine_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def drawPixel(self, x, y, pixelState):
		_x = ctypes.c_int(x)
		_y = ctypes.c_int(y)
		_pixelState = ctypes.c_int(pixelState)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_drawPixel
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _x, _y, _pixelState)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localdrawPixel_async(self, handle, ctx, res):

		if self._drawPixel_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._drawPixel_async(self, res, details)

	def drawPixel_async(self, x, y, pixelState, asyncHandler, ctx, fptr):
		if fptr == None:
			self._drawPixel_async = None
			self._ondrawPixel_async = None
		else:
			self._drawPixel_async = fptr
			self._ondrawPixel_async = self._asyncFactory(self._localdrawPixel_async)

		_x = ctypes.c_int(x)
		_y = ctypes.c_int(y)
		_pixelState = ctypes.c_int(pixelState)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_drawPixel_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._ondrawPixel_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def drawRect(self, x1, y1, x2, y2, filled, inverted):
		_x1 = ctypes.c_int(x1)
		_y1 = ctypes.c_int(y1)
		_x2 = ctypes.c_int(x2)
		_y2 = ctypes.c_int(y2)
		_filled = ctypes.c_int(filled)
		_inverted = ctypes.c_int(inverted)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_drawRect
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _x1, _y1, _x2, _y2, _filled, _inverted)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localdrawRect_async(self, handle, ctx, res):

		if self._drawRect_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._drawRect_async(self, res, details)

	def drawRect_async(self, x1, y1, x2, y2, filled, inverted, asyncHandler, ctx, fptr):
		if fptr == None:
			self._drawRect_async = None
			self._ondrawRect_async = None
		else:
			self._drawRect_async = fptr
			self._ondrawRect_async = self._asyncFactory(self._localdrawRect_async)

		_x1 = ctypes.c_int(x1)
		_y1 = ctypes.c_int(y1)
		_x2 = ctypes.c_int(x2)
		_y2 = ctypes.c_int(y2)
		_filled = ctypes.c_int(filled)
		_inverted = ctypes.c_int(inverted)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_drawRect_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._ondrawRect_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def flush(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_flush
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localflush_async(self, handle, ctx, res):

		if self._flush_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._flush_async(self, res, details)

	def flush_async(self, asyncHandler, ctx, fptr):
		if fptr == None:
			self._flush_async = None
			self._onflush_async = None
		else:
			self._flush_async = fptr
			self._onflush_async = self._asyncFactory(self._localflush_async)



		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_flush_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onflush_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getFontSize(self, font):
		_font = ctypes.c_int(font)
		_width = ctypes.c_int()
		_height = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getFontSize
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _font, ctypes.byref(_width), ctypes.byref(_height))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _width.value, _height.value

	def setFontSize(self, font, width, height):
		_font = ctypes.c_int(font)
		_width = ctypes.c_int(width)
		_height = ctypes.c_int(height)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setFontSize
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _font, _width, _height)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getFrameBuffer(self):
		_FrameBuffer = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getFrameBuffer
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_FrameBuffer))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _FrameBuffer.value

	def setFrameBuffer(self, FrameBuffer):
		_FrameBuffer = ctypes.c_int(FrameBuffer)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setFrameBuffer
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _FrameBuffer)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localsetFrameBuffer_async(self, handle, ctx, res):

		if self._setFrameBuffer_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._setFrameBuffer_async(self, res, details)

	def setFrameBuffer_async(self, FrameBuffer, asyncHandler, ctx, fptr):
		if fptr == None:
			self._setFrameBuffer_async = None
			self._onsetFrameBuffer_async = None
		else:
			self._setFrameBuffer_async = fptr
			self._onsetFrameBuffer_async = self._asyncFactory(self._localsetFrameBuffer_async)

		_FrameBuffer = ctypes.c_int(FrameBuffer)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setFrameBuffer_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsetFrameBuffer_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getHeight(self):
		_Height = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getHeight
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Height))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Height.value

	def initialize(self):
		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_initialize
			__func.restype = ctypes.c_int32
			result = __func(self.handle)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def saveFrameBuffer(self, frameBuffer):
		_frameBuffer = ctypes.c_int(frameBuffer)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_saveFrameBuffer
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _frameBuffer)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localsaveFrameBuffer_async(self, handle, ctx, res):

		if self._saveFrameBuffer_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._saveFrameBuffer_async(self, res, details)

	def saveFrameBuffer_async(self, frameBuffer, asyncHandler, ctx, fptr):
		if fptr == None:
			self._saveFrameBuffer_async = None
			self._onsaveFrameBuffer_async = None
		else:
			self._saveFrameBuffer_async = fptr
			self._onsaveFrameBuffer_async = self._asyncFactory(self._localsaveFrameBuffer_async)

		_frameBuffer = ctypes.c_int(frameBuffer)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_saveFrameBuffer_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onsaveFrameBuffer_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def getScreenSize(self):
		_ScreenSize = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getScreenSize
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_ScreenSize))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _ScreenSize.value

	def setScreenSize(self, ScreenSize):
		_ScreenSize = ctypes.c_int(ScreenSize)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setScreenSize
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _ScreenSize)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getSleeping(self):
		_Sleeping = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getSleeping
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Sleeping))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Sleeping.value

	def setSleeping(self, Sleeping):
		_Sleeping = ctypes.c_int(Sleeping)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_setSleeping
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _Sleeping)
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def getWidth(self):
		_Width = ctypes.c_int()

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_getWidth
			__func.restype = ctypes.c_int32
			result = __func(self.handle, ctypes.byref(_Width))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)

		return _Width.value

	def writeBitmap(self, xpos, ypos, xsize, ysize, bitmap):
		_xpos = ctypes.c_int(xpos)
		_ypos = ctypes.c_int(ypos)
		_xsize = ctypes.c_int(xsize)
		_ysize = ctypes.c_int(ysize)
		_bitmap = (ctypes.c_uint8 * len(bitmap))(*bitmap)

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_writeBitmap
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _xpos, _ypos, _xsize, _ysize, ctypes.byref(_bitmap))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localwriteBitmap_async(self, handle, ctx, res):

		if self._writeBitmap_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._writeBitmap_async(self, res, details)

	def writeBitmap_async(self, xpos, ypos, xsize, ysize, bitmap, asyncHandler, ctx, fptr):
		if fptr == None:
			self._writeBitmap_async = None
			self._onwriteBitmap_async = None
		else:
			self._writeBitmap_async = fptr
			self._onwriteBitmap_async = self._asyncFactory(self._localwriteBitmap_async)

		_xpos = ctypes.c_int(xpos)
		_ypos = ctypes.c_int(ypos)
		_xsize = ctypes.c_int(xsize)
		_ysize = ctypes.c_int(ysize)
		_bitmap = (ctypes.c_uint8 * len(bitmap))(*bitmap)


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_writeBitmap_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onwriteBitmap_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)

	def writeText(self, font, xpos, ypos, text):
		_font = ctypes.c_int(font)
		_xpos = ctypes.c_int(xpos)
		_ypos = ctypes.c_int(ypos)
		_text = ctypes.create_string_buffer(text.encode('utf-8'))

		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_writeText
			__func.restype = ctypes.c_int32
			result = __func(self.handle, _font, _xpos, _ypos, ctypes.byref(_text))
		except RuntimeError:
			raise

		if result > 0:
			raise PhidgetException(result)


	def _localwriteText_async(self, handle, ctx, res):

		if self._writeText_async == None:
			return
		_code = ctypes.c_int(res)
		_desc = ctypes.c_char_p()
		try :
			result = PhidgetSupport.getDll().Phidget_getErrorDescription(_code, ctypes.byref(_desc))
		except RuntimeError:
			raise
		details = _desc.value
		self._writeText_async(self, res, details)

	def writeText_async(self, font, xpos, ypos, text, asyncHandler, ctx, fptr):
		if fptr == None:
			self._writeText_async = None
			self._onwriteText_async = None
		else:
			self._writeText_async = fptr
			self._onwriteText_async = self._asyncFactory(self._localwriteText_async)

		_font = ctypes.c_int(font)
		_xpos = ctypes.c_int(xpos)
		_ypos = ctypes.c_int(ypos)
		_text = ctypes.create_string_buffer(text.encode('utf-8'))


		try:
			__func = PhidgetSupport.getDll().PhidgetLCD_writeText_async
			__func.restype = ctypes.c_int32
			res = __func(self.handle, _font, _character, _bitmap, self._onwriteText_async, None)
		except RuntimeError:
			self._setCharacterBitmap = None
			self._onsetCharacterBitmap = None
			raise

		if res > 0:
			raise PhidgetException(res)
