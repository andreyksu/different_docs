#-*- coding:utf-8 -*-

a = "glob"

if (a == "glob"):
	a = "if"
	bb = "c"
	print(a)

def parFunction():
	#nonlocal a
	a = "parent"	
	def childFunction():
		#nonlocal a
		a = "child"
		print(a)
	childFunction()
	print(a)

parFunction()
print(a)
print(bb)