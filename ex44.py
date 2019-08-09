#继承的3种交互方式：1.子类的动作完全等同父类的动作 2. 子类的动作完全覆盖了父类的动作 3. 子类的动作部分替换了父类的动作

#隐式继承：父类定义一个函数，但是在子类中没有定义#################################
# class Parent(object):
#     def implicit(self):
#         print("parent implicit()")
# class Child(Parent):
#     pass
#
# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()

#输出结果：
# parent implicit()
# parent implicit()
##################################################################


#显式覆盖：父类与子类有相同的函数名################################################
# class Parent(object):
#     def override(self):
#         print("parent override()")
# class Child(Parent):
#     def override(self):
#         print("child override()")
# dad = Parent()
# son = Child()
# dad.override()
# son.override()

#输出结果:
# parent override()
# child override()
#################################################################################

#利用super()调用父类的函数#########################################################
# class Parent(object):
#     def altered(self):
#         print("parent altered()")
# class Child(Parent):
#     def altered(self):
#         print("CHILD,BEFORE PARENT altered()")
#         super(Child,self).altered()
#         print("CHILD,AFTER PARENT altered()")
# dad = Parent()
# son = Child()
# dad.altered()
# son.altered()
#输出结果：
# parent altered()
# CHILD,BEFORE PARENT altered()
# parent altered()
# CHILD,AFTER PARENT altered()
####################################################################################

#####组合#######################################
class Other(object):
    def override(self):
        print("other override()")
    def implicit(self):
        print("other implicit()")
    def altered(self):
        print("other altered()")
class Child(object):
    def __init__(self):
        self.other = Other()              #将一个类定义成Child类的一个属性
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("child override()")
    def altered(self):
        print("child,before other altered()")
        self.other.altered()
        print("child,after other altered()")
son = Child()
son.implicit()
son.override()
son.altered()
###########################################################33
