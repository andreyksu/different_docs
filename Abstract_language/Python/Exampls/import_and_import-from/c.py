#-*- coding:utf-8 -*-
from a import x
# import a #при таком импорте, будут изменения в самом модуле а и в модуле b будет выводиться измененное значени.
import b

#a.x = 3
x = 3

#print('in module c::: a.x = ', a.x)
print('in module c::: x = ', x)

b.printX()