#dict style
mystuff = {'apple': "I am apples!"}
print(mystuff['apple'])

#module style
#this goes in mystuff.py
def apple():
    print("I am apples!")

tangerine = "Living reflection of a dream"

import mystuff
mystuff.apple()                           #利用module访问函数
print(mystuff.tangerine)                  #利用module访问变量

#class style

class Mystuff(object):

    def __init__(self):                                                   ##将类实例化得到object
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I am classy apples!")

thing = Mystuff()
thing.apple()
print(thing.tangerine)

##python查找Mystuff(),并知道了它是你定义的一个类
##python创建了一个空对象，里面包含了你在该类中用def指定的所有函数
##然后python回去检查你是不是在里面创建了一个__init__的函数，如果有创建，它就会调用这个函数，从而对你新创建的空对象实现了初始化
##Mystuff的__init__函数里，有一个多余的函数叫self,这就是python为你创建的空对象，可以为它设置一些变量
##在这里，我把self.tangerine设置成了一段歌词，这样我就初始化了该对象
##最后python将这个新建的对象赋予一个叫thing的变量
##类是一种蓝图或者一种预定义的东西，通过类可以创建新的迷你模块
##记住这不是拿一个类就直接使用，而是将类当作一个“蓝图”，然后用它创建和这个类有相同属性的副本
