# ##用继承的方式重写人和狗的属性
# class Animal:
#     """
#     人和狗都是动物，所以创造了一个Animal基类
#     """
#     def __init__(self,name,aggressivity,life_value):
#         self.name = name                #人和狗都有自己的名称，攻击力，生命值
#         self.aggressivity = aggressivity
#         self.life_value = life_value
#     def eat(self):
#         print('%s is eating' % self.name)
#
# class Dog(Animal):
#     def bite(self,people):              ##子类可以添加自己新的属性和方法（不会影响到父类）
#         people.life_value -= self.aggressivity
#
# class Person(Animal):
#     #思考如果我想在人这里增加money这个属性应该怎么做？？？？
#     def attack(self,dog):
#         dog.life_value -= self.aggressivity
#
# egg = Person('egon',10,1000)
# ha2 = Dog('二愣子',50,1000)
# egg.eat()
# ha2.eat()
# print(ha2.life_value)   #像ha2.life_value之类的属性引用，会先从实例中找life_value然后去类中找，然后再去父类中找...直到最顶级的父类。
# egg.attack(ha2)
# print(ha2.life_value)
