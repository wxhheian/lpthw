#python的类可以继承多个类，python的类如果继承了多个类，那么寻找方法是广度优秀（在python3中)
class A:
    def test(self):
        print('from A')
class B(A):
    def test(self):
        print('from B')
class C(A):
    def test(self):
        print('from C')
class D(B):
    def test(self):
        print('from D')
class E(C):
    def test(self):
        print('from E')
class F(D,E):
    # def test(self):
    #     print('from F')
    pass 

f1=F()
f1.test()
print(F.__mro__)  #查看类的线性继承
