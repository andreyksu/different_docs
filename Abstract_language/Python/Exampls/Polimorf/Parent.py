#-*- coding:utf-8 -*-

class TestClass:
	def test(self):
		print(u"--------------Это мтод родительского класса--------------")

	def startTest(self):
		try:
			self.test()			
		except (ZeroDivisionError, Exception) as e:
			print(u"--------------Перехватили Исключение--------------")
			print(e)

		else:
			print(u"Исключения так и не возникло")
