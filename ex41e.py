###继承####
#继承是一种创建新类的方式，在python中，新建的类可以继承一个或多个父类，父类又称为基类 或超类，新建的类称为派生类或子类
#继承分为单继承和多继承
# class ParentClass1:   #定义父类
#     pass
#
# class ParentClass2:   #定义父类
#     pass
#
# class SubClass1(ParentClass1):    #单继承，基类是ParentClass1  派生类是SubClass1
#     pass
#
# class SubClass2(ParentClass1,ParentClass2):    #多继承
#     pass
#
# print(SubClass1.__bases__)      #__base__只查看从左到右第一个父类， __bases___查看全部的父类
# print(SubClass2.__bases__)
#
# ##如果没有指定基类，python的类会默认继承object类
# print(ParentClass1.__bases__)
# print(ParentClass2.__bases__)


#继承例子说明
#猫可以：吃、喝、爬树
#狗可以：吃、喝、看家
#若要分别为猫和狗创建一个类。
#class 猫：
#    def 吃(self):
#         pass
#
#    def 喝(self):
#        pass
#
#     def 爬树(self):
#         pass
#
#class 狗：
#     def 吃(self):
#         pass
#
#    def 喝(self):
#        pass
#
#     def 看家(self)：
#        pass
# ##############但是猫和狗有共同的功能是吃和喝,则可以使用继承的功能
class Animal:
   def eat(self):
       print("%s 吃" %self.name)
   def drink(self):
       print("%s 喝" %self.name)

class Cat(Animal):                 #在类后面括号中写入另外一个类名，表示当前类继承另外一个类
    def __init__(self,name):
        self.name = name
        self.breed = '猫'
    def climb(self):
        print('爬树')

class Dog(Animal):                   #在类后面括号中写入另外一个类名，表示当前类继承另外一个类
    def __init__(self,name):
        self.name = name
        self.breed = '狗'
    def look_after_house(self):
        print('汪汪叫')

c1 = Cat('小白家的小黑猫')
c1.eat()
c2 = Cat('小黑家的小白猫')
c2.drink()
d1= Dog('胖子家的小瘦狗')
d1.look_after_house()
d1.eat()
