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
#Как вызвать innerFunc() - возможные способы?
def func3(param):
	print "param =====", param
	a = 333
	def innerFunc():
		print "innerFunc() =====", a
	a = 555
    
#--------------------------------------------------------
#Как поменять местами значения у 2х переменных (для определенности значение типа int), не прибегая к 3ей переменной:
# Есть переменная A и переменная B. Нужно в А поместить значение B, а в B значение из переменной А.

#--------------------------------------------------------
#Что выведет?
class Animal(object):
    def __init__(self):
        print('Animal.__init__')

class Wild(Animal):
    def __init__(self):
        print('Wild.__init__')

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print('Mammal.__init__')

class Tiger(Wild, Mammal):
    def __init__(self):
        super().__init__()
        print('Tiger.__init__')

tiger = Tiger()






#--------------------------------------------------------
#Что выведет?
class Animal(object):
	def __init__(self):
		print('Animal.__init__')

class Wild(Animal):
    def say(self):
        print('Wild.spam')
        super().say()

class Mammal(Animal):
    def say(self):
        print('Mammal.spam')

class Tiger(Wild, Mammal):
    pass

wild = Wild()
wild.say()

tiger = Tiger()
tiger.say()