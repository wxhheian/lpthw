#抽象类：抽象类是一个特殊的类，他的特殊之处在于只能被继承，不能被实例化，且子类必须实现抽象方法
#如果说类是从一堆对象中抽取相同的内容而来，那么抽象类就是从一堆类中抽取相同的内容而来，包括数据属性和函数属性。抽象类是基于类抽象而来。
#比如我们有香蕉的类，有苹果的类，有桃子的来，从这些类抽取相同的内容就是水果的类。


#一切皆文件
import abc   #利用abc模块实现抽象类
class All_file(metaclass=abc.ABCMeta):
    all_type = 'file'
    @abc.abstractmethod   #定义抽象方法，无需实现功能
    def read(self):
        """子类必须定义读功能"""
        pass

    @abc.abstractmethod #定义抽象方法，无需实现功能
    def write(self):
        """子类必须定义写功能"""
        pass

# class Txt(All_file):
#     pass
#
# t1 = Txt()                  #报错，子类没有定义抽象方法

class Txt(All_file): #子类继承抽象类，但必须定义read write
    def read(self):
        print('文本数据的读取方法')
    def write(self):
        print('文本数据的读取方法')
class Sata(All_file):
    def read(self):
        print('硬盘数据的读取方法')
    def write(self):
        print('硬盘数据的读取方法')
class Process(All_file):
    def read(self):
        print('进程数据的读取方法')
    def write(self):
        print('进程数据的读取方法')

wenbenwenjian = Txt()
yingpanwenjian = Sata()
jinchengwenjian = Process()

#这样大家都被归一化了，也就是一切皆文件的思想
wenbenwenjian.read()
yingpanwenjian.write()
jinchengwenjian.read()

print(wenbenwenjian.all_type)
print(yingpanwenjian.all_type)
print(jinchengwenjian.all_type)

#抽象类的本质还是类，指的是一组类的相似性，包括数据属性（all_type），也包括函数属性（read.write),而接口只强调函数属性的相似性
