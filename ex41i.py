#继承有两种用途：
#1.继承基类的方法，并且做出自己的改变或拓展
#2.申明某个子类兼容于某基类，定义一个接口类（Interface),接口类中定义了一些接口名（就是函数名）且并未实现接口的功能，子类继承接口类，并且实现接口中的功能
# #####################################################################
# class Alipay:   #接口类
#     """支付宝支付"""
#     def pay(self,money):
#         print('支付宝支付了%s元' % money)
# class Applepay:      #接口类
#     """apple pay 支付"""
#     def pay(self,money):
#         print('apple pay支付了%s元' %money)
#
# def pay(payment,money):      #payment是一个类   注意这了的pay函数与上面class里的函数名字一样
#     """支付函数，总体负责支付，对应支付的对象和要支付的金额"""
#     payment.pay(money)
#     print('执行这一条')
#
# p = Applepay()
# # p.pay(200)
# pay(p,300)     #与18行代码功能一样
#################################################################################

#####################################################
# class Alipay:   #接口类
#     """支付宝支付"""
#     def pay(self,money):
#         print('支付宝支付了%s元' % money)
# class Applepay:      #接口类
#     """apple pay 支付"""
#     def pay(self,money):
#         print('apple pay支付了%s元' %money)
# class Wechatpay:
#     def fuqian(self,money):
#         """实现了pay的功能，但是名字不一样"""
#         print('微信支付了%s元' %money)
#
# def pay(payment,money):      #payment是一个类
#     """支付函数，总体负责支付，对应支付的对象和要支付的金额"""
#     payment.pay(money)
#
#
# p = Wechatpay()
# pay(p,200)           #执行报错 'Wechatpay' object has no attribute 'pay'
##########################################################


######################################################
# class Payment:
#     def pay(self):
#         raise NotImplementedError
#
# class Wechatpay(Payment):                #继承
#     def fuqian(self,money):
#         print('微信支付了%s元' %money)
#
# p = Wechatpay()            #这里正常运行
# pay(p,200)                ##这里报错  name 'pay' is not defined
###############################################################

###################借用abc模块来实现接口################################
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self,money):
        pass
class Wechatpay(Payment):
    def fuqian(self,money):
        print('微信支付了%s元' %money)
p = Wechatpay()     #这里就报错了   Can't instantiate abstract class Wechatpay with abstract methods pay
#########################################################
