##python中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的
#L(Local):局部作用域
#E(Enclosing):闭包函数外的函数中
#G(Global):全局作用域
#B(Built-in):内置作用域，内置函数所在的范围
#以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。

##################eg.1#####################
g_count = 0    #全局作用域
def outer():
    o_count = 1    #闭包函数外的函数中
    def inner():
        i_count = 2   #局部作用域

################################################

##内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它
#>>>import builtins
#>>>dir(builtins)

###########eg2########################
#Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，
>>>if True:
... msg = 'I AM FROM RUNOOB'
...
>>>msg
'I AM FROM RUNOOB'

##实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
#如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
>>> def test():
...    msg_inner = 'i am from runoob'
...
>>>msg_inner
#报错

#####################################################


################eg.3###############

total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)

###输出结果
函数内是局部变量 :  30
函数外是全局变量 :  0

####################################################

############eg4#################################
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)
#输出结果：
1
123
123

########################################################

##################eg5##############################
##如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
##输出结果：
100
100
##############################################

#####eg##################
globals()  返回全局变量的字典
>>>a = 'runobb'
>>>globals()
输出结果：
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'a': 'runoob'}
#########################################

#######################items()#################
#items()函数以列表返回可遍历的(键, 值) 元组数组
