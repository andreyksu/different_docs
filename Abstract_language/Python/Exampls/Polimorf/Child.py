#-*- coding:utf-8 -*-

import Parent

class SomeTest(Parent.TestClass):
	def test(self):
		print(u"--------------Это метод дочернего класса--------------")		
		self.a = 1/0

if __name__ == '__main__':
	someTest = SomeTest()
	someTest.startTest()