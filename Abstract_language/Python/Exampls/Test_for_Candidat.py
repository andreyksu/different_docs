#-*- coding:utf-8 -*-

#Что будет выведено?

a = [1, 2, 3]

def func1():
	a = [5, 6]
	print "func1 a =====", a
	def inner_func1():
		a[1:1] = [7, 8]
		print "inner_func1 a =====", a
	inner_func1()

func1()

print "a", "=====", a


#--------------------------------------------------------
#Что выведет:
i = [1, 2, 3]
def func2(arg = i):
	length = len(arg)
	arg[length:] = [4, 5]
	print "arg =====", arg

func2()
i = [100, 200, 300]
func2()


#--------------------------------------------------------
def func3(param):
	print "param =====", param
	a = 333
	def innerFunc():
		print "innerFunc() ", a
	a = 555

	return innerFunc
	#return lambda a, param=param: a+param

result = func3(444)
result()


	