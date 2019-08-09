#多态指的是一类事物有多种形态
#动物的多种形态：人，狗，猪
import abc
class Animal(metaclass=abc.ABCMeta):            #同一类事物：动物
    @abc.abstractmethod
    def talk(self):
        pass
class People(Animal):         #动物的形态之一：人
    def talk(self):
        print('say hello')
class Dog(Animal):            #动物的形态之一：狗
    def talk(self):
        print('say wangwang')
class Pig(Animal):             #动物的形态之一：猪
    def talk(self):
        print('say aoao')


#文件有多种形态：文本文件，可执行文件
class File(metaclass=abc.ABCMeta):      #同一类事物：文件
    @abc.abstractmethod
    def click(self):
        pass
class Text(File):        #文件的形态之一：文本文件
    def click(self):
        print('open file')
class ExeFile(File):   #文件的形态之一：可执行文件
    def click(self):
        print('execute file')

#多态性：向不同对象发送同一条消息，不同对象在接收时会产生不同的行为（函数）
#比如：老师.下课铃响了（），学生.下课铃响了（），老师执行的是下班操作，学生执行的是放学操作

peo = People()
dog = Dog()
pig = Pig()
peo.talk()       #peo,dog,pig都是动物，只要是动物肯定有talk方法，于是不用考虑它们三个的具体类型，而直接使用talk方法
dog.talk()
pig.talk()
#更进一步，我们可以定义一个统一的接口来使用
def func(obj):
    obj.talk()

func(peo)
