#-*-coding:utf-8-*-

class Base(object):
	def __init__(self):
		print('Base.__init__')

class A(Base):
    def spam(self):
        print('A.spam')
        super().spam()

class B(Base):
    def spam(self):
        print('B.spam')

class C(A, B):
    pass

y = C()
y.spam()