#-*-coding:utf-8-*-

#import ru.annikonenkov.secondmodule.SecondModule as sm
import ru.annikonenkov.secondmodule as mm #См. __init__.py

def myFuncInFirstModule():
	#sm.myFuncInSecondModule()	
	mm.SecondModule.myFuncInSecondModule()
	print("myFuncInFirstModule")
	path = mm.__path__
	file = mm.SecondModule.__file__
	name = mm.SecondModule.__name__	
	print(path, file, name)

def plusFunc(i, j):
	return i + j