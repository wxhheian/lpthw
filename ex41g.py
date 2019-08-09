########super()#############################################
#子类执行父类的方法可以用super()方法
#example1:
class A:
    def hahaha(self):
        print('A')

class B(A):
    def hahaha(self):
        #super().hahaha()
        #A.hahaha(self)
        super(B,self).hahaha()
        print('B')

# a = A()             
b =B()
b.hahaha()
super(B,b).hahaha()
###############################################

##example2:##################################
# class A:
#     def add(self,x):
#         y = x + 1
#         print(y)
# class B(A):
#     def add(self,x):
#         super().add(x)
# b = B()
# b.add(2)
#输出结果：
#3
##################################################

#example3:
# class FooParent:
#     def __init__(self):
#         self.parent = 'I\'m the parent.'
#         print('Parent')
#     def bar(self,message):
#         print("%s from Parent" % message)
#
# class FooChild(FooParent):
#     def __init__(self):
#         #super(FooChild,self)首先找到FooChild的父类，即FooParent,然后把对象转为FooParent的对象
#         super(FooChild,self).__init__()
#         print('child')
#
#     def bar(self,message):
#         super(FooChild,self).bar(message)
#         print('child bar function')
#         print(self.parent)
#
# fooChild = FooChild()
# fooChild.bar('helloworld')
#####################################################


##example4:
#python子类调用父类成员有两种方法，分别是普通方法和super()方法
# class Base:
#     def __init__(self):
#         print('Base init')

#普通方法
# class Leaf(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print('leaf init')
#super方法
# class Leaf(Base):
#     def __init__(self):
#         super(Leaf,self).__init__()
#         print('Leaf init')
#
# leaf = Leaf()
##############################################

##example5:钻石继承的难题
# class Base:
#     def __init__(self):
#         print('Base init')
#
# class Medium1(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Medium1 init")
#
# class Medium2(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Medium2 init")
#
# class Leaf(Medium1,Medium2):
#     def __init__(self):
#         Medium1.__init__(self)
#         Medium2.__init__(self)
#         print("Leaf init")
#
# leaf = Leaf()
# 输出结果：
# Base init
# Medium1 init
# Base init
# Medium2 init
# Leaf init             ##Base被初始化了两次
################################################

##example6:钻石继承的难题解决
# class Base:
#     def __init__(self):
#         print('Base init')
#
# class Medium1(Base):
#     def __init__(self):
#         super(Medium1,self).__init__()
#         print("Medium1 init")
#
# class Medium2(Base):
#     def __init__(self):
#         super(Medium2,self).__init__()
#         print("Medium2 init")
#
# class Leaf(Medium1,Medium2):
#     def __init__(self):
#         super(Leaf,self).__init__()
#         print("Leaf init")
#
# leaf = Leaf()
#输出结果：
# Base init
# Medium2 init
# Medium1 init
# Leaf init
