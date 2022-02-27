#-*- coding:utf-8 -*-

class ClassA:
	data = 'spam'

	def __getattr__(self, name):
		print("__getattr__ name = %s" % name)
		return getattr(self.data, name)

	def __getitem__(self, index):
		print("__getitem__  index = %s" % index)
		return self.data[index:index+1]

X = ClassA()
res = X[2] #Вот в Python3 если бы метода __getitem__ не был бы объявлен, то метод __getattr__ не был бы вызван для поиска __getitem__. А в python2 __getitem__ использовался бы для поиска __getitem__.
res_1 = type(X).__getitem__(X, 2) #А это прямое общращение к __getitem__ оно нормально работает в Python3