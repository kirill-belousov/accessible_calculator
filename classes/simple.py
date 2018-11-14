import wx
from .func import *

class Simple(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		text = wx.TextCtrl(self, value="текст для теста на вкладке simple", name="Выражение")
		answer = wx.TextCtrl(self, style=wx.TE_READONLY, name="Ответ")
		