import wx

class Trigonometry(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		text = wx.TextCtrl(self, value="текст для теста на вкладке trig")