import math
import vector3d
import numpy

def expression(s):
	try: r = eval(s)
	except Exception: r = "Проверьте правильность введённого выражения. Произошла ошибка при попытке посчитать."
	finally: return r