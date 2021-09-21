#-*-coding:utf-8-*-

import sys, os
sys.path.append('/root/AutoTest/src')

import ru.annikonenkov.firstmodule.FirstModule as fm
import pytest

@pytest.fixture(scope="function") #function, class, module, package, session
def get_array():
	return list('C')

class TestClassPluss:
	someParam = "someParam"

	def test_plus(self, get_array):		
		get_array.append("A")
		print(get_array)
		self.someParam = 1
		print("Test-----test_plus")
		assert fm.plusFunc(1, 3) == 4

	def test_plus_1(self, get_array):
		get_array.append("B")
		print(get_array)
		print(self.someParam)
		print("Test-----test_plus_1")
		assert fm.plusFunc(1, 3) != 5

def test_plus_2():
	print("Test-----test_plus_2")
	assert fm.plusFunc(1, 3) == 4

