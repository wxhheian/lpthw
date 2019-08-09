class Person:
    role = 'person'

    def __init__(self,name,aggressivity,life_value,money):
        self.name = name
        self.aggressivity = aggressivity
        self.life_value = life_value
        self.money = money

    def attack(self,dog):
        #人可以攻击狗, dog is a object
        dog.life_value -= self.aggressivity

class Dog:
    role = 'dog'

    def __init__(self,name,breed,aggressivity,life_value):
        self.name = name
        self.breed = breed
        self.aggressivity = aggressivity
        self.life_value = life_value

    def bite(self,people):
        #people is a object
        people.life_value -= self.aggressivity

class Weapon:
    def __init__(self,name,price,aggrev,life_value):
        self.name = name
        self.price = price
        self.aggrev = aggrev                #武器的攻击加成
        self.life_value = life_value

    def update(self,obj):   #obj就是要带这个装备的人,是个对象
        obj.money -= self.price   #用这个武器的obj要花钱买武器
        obj.aggressivity += self.aggrev    ##武器的攻击加成
        obj.life_value += self.life_value    #武器的生命加成

    def prick(self,obj):            #该装备的主动技能,攻击力为500
        obj.life_value -= 500


##交互测试
lance = Weapon('长矛',200,6,100)
egg = Person('egon',10,1000,600)
ha2 = Dog('二愣子','哈士奇',10,1000)

#egg独自力战二愣子深感吃力，决定买个装备
if egg.money > lance.price:
    lance.update(egg)
    egg.weapon = lance     #增加egg的属性weapon,将对象lance赋给属性

print(egg.money,egg.life_value,egg.aggressivity)
print(ha2.life_value)
egg.attack(ha2)
print(ha2.life_value)
egg.weapon.prick(ha2)
print(ha2.life_value)
