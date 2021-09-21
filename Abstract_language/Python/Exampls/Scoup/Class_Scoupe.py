#-*- coding:utf-8 -*-
b="In Module"

class ParentClass:

	class InnerClass:
		b = "InnerClass"
		def __init__(self):
			print("InnerClass")

		def inClassMethod(self):
			print("inClassMethod")

	b = "In Class"
	def __init__(self):
		print("Constructor")

	def myFunc(self):
		print(b)#Глобальная область видимости для метода - это глабальное пространсво имен модуля. В котором определен объемлющий класс.
		#Для метода все так же как и для функции. Это нужно когда у нас в модуль импортируется др. модуль - и что бы метод имел доступ.
		print(ParentClass.b)
		innerClass = ParentClass.InnerClass()
		return innerClass

	def method(x):
			strr = "str"
			print("method")
			for x in strr:
				print(x)
			for i in range(len(strr)):
				print(strr[i])


aa = ParentClass()
inCl = aa.myFunc()
print(b)
print(ParentClass.b)
inCl.inClassMethod()

ParentClass.method(aa)
#aa.myFunc1()

