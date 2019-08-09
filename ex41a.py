##################################################
from math import pi
class Circle:
    '''定义了一个圆形类；提供计算面积和周长的方法'''
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi*self.radius*self.radius

    def perimeter(self):
        return 2*pi*self.radius

# circle = Circle(10)    #实例化
# area1 = circle.area()
# per1 = circle.perimeter()
# print(area1,per1)
#######################################################

###################组合#############
class Ring:
    def __init__(self,radius_outside,radius_inside):         ##radius_outside是参数
        self.outside_circle = Circle(radius_outside)     ##outside_circle是属性   将一个对象赋于属性，于是可以用该对象的所有方法和属性
        self.inside_circle = Circle(radius_inside)

    def area(self):
        return self.outside_circle.area() - self.inside_circle.area()

    def perimeter(self):
        return self.outside_circle.perimeter() - self.inside_circle.perimeter()

ring = Ring(10,5)
print(ring.area())
print(ring.perimeter())
