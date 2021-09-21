#-*-coding:utf-8-*-

import sys, os
sys.path.append('/root/AutoTest/src')

import ru.annikonenkov.firstmodule.FirstModule as fm
import pytest

class TestClassPluss:

#==================================================================================
#=====Эти методы работают только для тестов вне класса, в случае класса работать не будут=============================
	def setup_module():
		print("setup_module: whole.py The module is executed only once")
		print("====================*********************====================")

	def teardown_module():
		print("teardown_module: whole.py The module is executed only once")
		print("====================*********************======================")

	def setup_function():
		print("setup_function: Each use case is executed before it starts")

	def teardown_function():
		print("teardown_function: It is executed at the end of each use case")
#==================================================================================
#=====Эти методы работают только для тестов вне класса=============================
	@classmethod
	def setup(self):
		print("Each_InClass_____setup: Execute before each use case begins And Before setup_method")

	@classmethod
	def teardown(self):
		print("Each_InClass_____teardown: Execute at the end of each use case begins And Before teardown_method")

	@classmethod
	def setup_class(cls):
		print("Class_____setup_class: All use case execution============before")

	@classmethod
	def teardown_class(cls):
		print("Class_____teardown_class: All use case execution=============after")

	def setup_method(self):
		print("Method_____setup_method:  Execute before each use case begins")

	def teardown_method(self):
		print("Method_____teardown_method:  Execute at the end of each use case")
#==================================================================================
	def test_plus(self):
		print("Test-----test_plus")
		assert fm.plusFunc(1, 3) == 4

	#@pytest.mark.slow
	def test_plus_1(self):
		print("Test-----test_plus_1")
		assert fm.plusFunc(1, 3) != 5

#if __name__ == "__main__":
#	pytest.main(["-s", "test_first.py"])

def setup_module():
	print("====================*********************====================")
	print("Module_____setup_module: whole.py The module is executed only once")
	print("====================*********************======================")


def teardown_module():
	print("====================*********************======================")
	print("Module_____teardown_module: whole.py The module is executed only once")
	print("====================*********************======================")

def setup_function():
	print("Procedure_____setup_function: Each use case is executed before it starts")

def teardown_function():
	print("Procedure_____teardown_function: It is executed at the end of each use case")

def test_plus_2():
	print("Test-----test_plus_2")
	assert fm.plusFunc(1, 3) == 4