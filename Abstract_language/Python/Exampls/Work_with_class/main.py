#-*- coding:utf-8 -*-

class ParentClass:
	aa = 'ParentClass__aa'
	bb = "ParentClass__bb"

	def __init__(self):
		print("ParentClass > init")

	def printParam(self):
		print('ParentClass.aa = ', ParentClass.aa)
		print('self.aa = ', self.aa) #1
		# Лутц т2. Абстрактные суперклассы. стр 106. дает пояснение: Каждый раз self осуществляте поиск с текущего экземпляра и вверх. Вот и принчина вывода а этой строчке именно aa = 'MyFirstClass'.
		# Т.е. здесь интерпретатор увидел self и пошел искать снова с класса MyFirstClass ну а у этого класса есть своя переменная, найдя ее, поиск останавливается.
		# Класс - играет роль фабрик экземпляров. Их атрибуты - данные и функции, наследуются всеми экземплярами, созданными от них.

	def doSomething(self):
		self.action()


class MyFirstClass(ParentClass):

	aa = 'MyFirstClass'

	def __init__(self, a, b):
		super().__init__() #А можно и так super(MyFirstClass, self).__init__() где первый параметр, это класс относительно которого будет искаться метод и вверх. Это полезно при множественном наследовании, когда хотим точно указать где искать. если методы у веток от которых наследуемся могут совпадать.
		self.a = a
		self.b = b
		self.aa = 'MyFirstClass > __init__' #Здесь по сути переопределили/перекрыли переменную класса, переменной экземпляра. Дальше где будет self.aa будет обращение уже к этой переменной а не к переменной класса. 

	def printParam(self):
		ParentClass.printParam(ParentClass)
		ParentClass.printParam(self) 	#Cм. (#1) Любоптынй момент. В данном случае, будет выведено значение из текущего класса а не из ParentClass. 
										#Эту проблему решает замена аа на __аа. Два подчеркивания интепретатор заменяет на имя класса, что делает уникальным поле или ментод
										#Но если переменная должна быть public - то пока не очень понятно как уходить от этой проблемы.
										#Видимо обращение к переменной класса через имя класса.
		print('ParentClass.aa = ', ParentClass.aa)
		print('MyFirstClass.aa = ', MyFirstClass.aa)
		print('self.aa = ', self.aa)
		print('self.a = ', self.a)
		print('self.b = ', self.b)

	def action(self):
		print("PrintFromAction")

	def action1(self):
		self.action()


if __name__ == '__main__':
	x = MyFirstClass(2, 3)
	x.printParam()
	print('--------------------------------')	
	print(x.__dict__)
	print('--------------------------------')
	x.doSomething()
	x.action1()

	class_1 = x.__class__
	dict_1 = x.__class__.__dict__	
	itIsTuple = x.__class__.__bases__
	class_2 = x.__class__.__bases__.__class__ #Т.к. __bases__ возвращает tuple, дальше уже идет работа с tuple. Т.е. здесь у tuple получаем класс.
	dict_3 = x.__class__.__bases__.__class__.__dict__ #Здесь получается мы так же выводим информацию о tuple.

	print('x.__class__ = %s' % class_1)
	print('--------------------------------')
	print('x.__class__.__dict__ = %s' % dict_1)
	print('++++++++++++++++++++++++++++++++')
	print('x.__class__.__bases__ = %s' % itIsTuple)
	print('================================')	
	for i in itIsTuple:
		print('>>>>>>>>>>>>> У tuple только один родитель видимо >>>>>>>>>>>>>')
		print('i.__dict__ = %s' % i.__dict__)
		print('i.__class__ = %s' % i.__class__)
		print('i.__class__.__name__ = %s' % i.__class__.__name__)
		print('i.__class__.__dict__ = %s' % i.__class__.__dict__)
		print('>>>>>>>>>>>>>')
	print('################################')
	print('x.__class__.__bases__.__class__ = %s' % class_2)
	print('********************************')
	print('x.__class__.__bases__.__class__.__dict__ = %s' % dict_3)
	print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
	print(type(itIsTuple))

