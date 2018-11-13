import wx
from classes import *

def main():
	app = wx.App()
	w = MainWindow(title="Доступный калькулятор")
	w.Show(True)
	app.MainLoop()

if __name__ == "__main__": main()