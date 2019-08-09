class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, aggressivity, life_value):
        self.name = name  # 每一个角色都有自己的昵称;
        self.aggressivity = aggressivity  # 每一个角色都有自己的攻击力;
        self.life_value = life_value  # 每一个角色都有自己的生命值;
        self.weapon = Weapon()

    def attack(self,dog):
        # 人可以攻击狗，这里的狗也是一个对象。dog is a object
        # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
        dog.life_value -= self.aggressivity



class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性都是狗

    def __init__(self, name, breed, aggressivity, life_value):
        self.name = name  # 每一只狗都有自己的昵称;
        self.breed = breed  # 每一只狗都有自己的品种;
        self.aggressivity = aggressivity  # 每一只狗都有自己的攻击力;
        self.life_value = life_value  # 每一只狗都有自己的生命值;

    def bite(self,people):
        # 狗可以咬人，这里的人也是一个对象。 people is a object
        # 狗咬人，那么人的生命值就会根据狗的攻击力而下降
        people.life_value -= self.aggressivity


class Weapon:
    def prick(self, obj):  # 这是该装备的主动技能,扎死对方      #在一个类中以另外一个类的对象作为数据属性，称为类的组合
        obj.life_value -= 500  # 假设攻击力是500



###########人狗简单交互###########
egg = Person('egon',10,1000)
ha2 = Dog('二愣子','哈士奇',10,10000)
print(ha2.life_value)         #看看ha2的生命值
egg.attack(ha2)               #egg打了ha2一下
print(ha2.life_value)         #ha2掉了10点血
##############################################

##################组合####################
egg = Person('egon',10,1000)
ha2 = Dog('二愣子','哈士奇',10,10000)
print(ha2.life_value)
egg.weapon.prick(ha2)
print(ha2.life_value)
#egg组合了一个武器的对象，可以直接egg.weapon来使用组合类中的所有方法
######################################################
