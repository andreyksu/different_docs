from distutils.core import setup, Extension

setup(name="spam",
	version="1.0",
	py_modules = ['spam.py'],
	ext_modules = [
		Extension("_spam", ["spammodule.c"])
	]
)