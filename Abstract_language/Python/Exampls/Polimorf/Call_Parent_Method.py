#-*- coding:utf-8 -*-
class Carr:

	def __init__(self, init):
		print (u"Parent consructor Car")
		self.aaa = init
		print(self.aaa)

	def tmp_method(self):
		print (u"Parent tmp_method()")

class SmallCar(Carr):
	def __init__(self, ini):		
		#Carr.__init__(self, ini)#Python2
		super(SmallCar, self).__init__(ini)#Pyhon3
		self.aaa = 333#По сути это та же переменная. Т.е. не создается новая переменная
		print ("Child consructor SmallCar ")
		print (self.aaa)

	def tmpp_method(self):
		super(SmallCar, self).tmp_method()#Python3
		print (u"Child tmp_method()")


if __name__ == '__main__':
	a_car = SmallCar(222)
	a_car.tmpp_method()

#a_car.second("Second")