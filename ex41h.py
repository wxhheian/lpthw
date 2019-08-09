##人狗大战重写(通过继承，super方法)
class Animal:
    """人和狗都是动物，所以创造一个Animal基类"""
    def __init__(self,name,aggressivity,life_value):
        self.name = name              #人和狗都有昵称，攻击力，生命
        self.aggressivity = aggressivity
        self.life_value = life_value
    def eat(self):                #人和狗都会吃
        print('%s is eating' %self.name)

class Dog(Animal):
    """狗类，继承Animal类"""
    def __init__(self,name,breed,aggressivity,life_value):
        super().__init__(name,aggressivity,life_value)         #执行父类Animal的init方法
        self.breed = breed     #派生出新的属性
    def bite(self,people):
        """派生出新的方法"""
        people.life_value -= self.aggressivity
    def eat(self):
        super().eat()
        #Animal.eat(self)
        print('from Dog')

class Person(Animal):
    """人类，继承Animal"""
    def __init__(self,name,aggressivity,life_value,money):
        super().__init__(name,aggressivity,life_value)
        #Animal.__init__(self,name,aggressivity,life_value)
        #super(Person,self).__init__(name,aggressivity,life_value)
        self.money = money
    def attack(self,dog):
        """派生出了新的方法"""
        dog.life_value -= self.aggressivity
    def eat(self):
        Animal.eat(self)
        print('from Person')
egg = Person('egon',10,1000,600)
ha2 = Dog('二愣子','哈士奇',50,1000)
print(egg.life_value)
ha2.bite(egg)
print(egg.life_value)
