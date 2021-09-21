#-*- coding:utf-8 -*-
class MyClass:
    fistAttr = 11 # Атрибут класса(в терминалогии Java - static)
    secondAttr = 22 # Атрибут класса(в терминалогии Java - static)
    def function1(self):    
        #print(fistAttr) - так нельзя, говорит о неизвестности данного атрибута.
        print("MyClass.fistAttr = {}".format(MyClass.fistAttr))
        print("MyClass.secondAttr = {}".format(MyClass.secondAttr))
        print("self.secondAttr = {}".format(self.secondAttr))


        print("************************************************")
        print("Выполняем MyClass.fistAttr + 1 и MyClass.secondAttr + 1")
        MyClass.fistAttr = MyClass.fistAttr + 1         # Получается, что при данном использовании, это аналог public static
        MyClass.secondAttr = MyClass.secondAttr + 1     # Получается, что при данном использовании, это аналог public static
        print("MyClass.fistAttr = {}".format(MyClass.fistAttr))
        print("MyClass.secondAttr = {}".format(MyClass.secondAttr))
        print("self.secondAttr = {}".format(self.secondAttr))   #Ну и как в Java - можно через объект обратиться к static полю.


        print("************************************************")
        print("Объявляем self.secondAttr = self.secondAttr + 1")
        self.secondAttr = self.secondAttr + 1           # Выходит так, что мы создаем переменную экземпляра, перекрывая при этом переменную класса.
                                                        # А так нельзя self.secondAttr = secondAttr + 1
        print("MyClass.fistAttr = {}".format(MyClass.fistAttr))
        print("MyClass.secondAttr = {}".format(MyClass.secondAttr))
        print("self.secondAttr = {}     <<<<<".format(self.secondAttr))
        print("Выходит так. что объявление вида self.secondAttr перекрывает secondAttr уровня класса")
        

        print("************************************************")
        print("Вутри метода объявляем переменную уровня экземпляра класса self.thirdParam и локальную переменную метода fourth")
        self.thirdParam = 33    # Атрибут экземпляра, в рамках экземпляра, доступен в других методах. Хоть и объявлен в текущем методе.
        fourth = 44             # Тоже переменная экземпляра, но создана в лок. видимости текущего метода, и доступа к ней из function2 - нет.
        self.thirdParam = self.thirdParam + 1
        print("self.thirdParam + 1 = {}".format(self.thirdParam))   # Без self нельзя, будет ошибка. Вроде логично.
        print("fourth + 1 = {}".format(fourth + 1))                     # А здесь нельзя ставить self, так как это локальная переменная метода и доступ к ней извне не возможен

        print("************************************************")
        print("Before innerFunction - внутри вложенного метода создаем новую переменную self.thirdParam = 500")
        def innerFunction():
            self.thirdParam = 500;  
            thirdParam = 600;
            print("self.thirdParam = {}".format(self.thirdParam))
            self.thirdParam = self.thirdParam + 1;
            print("self.thirdParam + 1 = {}".format(self.thirdParam))   # Без self нельзя, будет ошибка. Вроде логично.

        print("Внутри метода function1 вызываем внутренний метод innerFunction")
        innerFunction()

        print("************************************************")
        print("After innerFunction")        
        self.thirdParam = self.thirdParam + 1;
        print("self.thirdParam + 1 = {}".format(self.thirdParam))   # Без self нельзя, будет ошибка. Вроде логично.

        #return innerFunction

    def function2(self):        
        print("MyClass.fistAttr = {}".format(MyClass.fistAttr))
        print("MyClass.secondAttr = {}     <<<<<".format(MyClass.secondAttr))
        print("self.secondAttr = {}     <<<<<".format(self.secondAttr))
        self.thirdParam = self.thirdParam + 1;
        print("self.thirdParam + 1 = {}".format(self.thirdParam))  # Вызов function2 до вызова function1 даст ошибку, так как thirdParam еще не создан. Он создается при первом присваивании.
        #print(MyClass.fourth)

    @staticmethod
    def function3():
        print("function3()")

    @classmethod
    def function4(self):
        print("function4()")


x=MyClass()
x.function1()
#x.function2()
print("---------------------------------------------")
#MyClass.function2(x)        #А можно и так вызвать метод, передав непосредственно экземпляр.
print("---------------------------------------------")
MyClass.function3()
MyClass.function4()
print("---------------------------------------------")
print("MyClass.fistAttr = {}".format(MyClass.fistAttr))
print("MyClass.secondAttr = {}     <<<<<".format(MyClass.secondAttr))


print("---------------------------------------------")
print("---------------------------------------------")
print("---------------------------------------------")
y=MyClass()
y.function1()