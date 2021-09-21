#-*-coding:utf-8-*-

class Base(object):
	def __init__(self):
		print('Base.__init__')

class A(Base):	
	a = "a"
	def __init__(self):
		self.aa = "aa"
		aaa = "aaa"
		print('A.__init__')

class B(Base):	
	def __init__(self):
		super().__init__()
		print('B.__init__')

class C(A, B):
	def __init__(self):
		super().__init__()
		print('C.__init__')

x = C()
print(x.a)
print(x.aa)
print(x.aaa)

print(C.__mro__)