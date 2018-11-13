import wx
from classes import *

def main():
	w = MainWindow(title="Доступный калькулятор")
	app = wx.App()
	w.show(True)
	app.MainLoop()

if __name__ = "__main__: main()