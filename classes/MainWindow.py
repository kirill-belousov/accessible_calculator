import wx
from .simple import Simple
from .trigonometry import Trigonometry

class MainWindow(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, title=title)
		p = wx.Panel(self)
		nb = wx.Notebook(p)
		simple = Simple(nb)
		trig = Trigonometry(nb)
		
		nb.AddPage(simple, "Простая арифметика")
		nb.AddPage(trig, "Тригонометрия")
		
		sizer = wx.BoxSizer()
		sizer.Add(nb, 1, wx.EXPAND)
		p.SetSizer(sizer)
		