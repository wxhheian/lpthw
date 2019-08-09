#############################with  as  ################################
with语句是什么？
example1:
>>>file = open("/tmp/foo.txt")
>>>data=file.read()
>>>file.close()                 #有两个缺点：1. 忘记关闭文件句柄   2.文件读取发生异常

example2:
file  = open("/tmp/foo.txt")
try:
    data = file.read()
finally:
    file.close()                           ##比example1好在于无论读取文件是否异常，都关闭文件句柄

with的基本思想是with所求值的对象必须有一个__enter__()方法，一个__exit__()方法。
紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
example3:
class Sample:
    def __enter__(self):
        print("In __enter__()")
        return "Foo"

    def __exit__(self, type, value, trace):
        print("In __exit__()")

def get_sample():
    return Sample()

with get_sample() as sample:
  print("sample:", sample)

输出结果：
In __enter__()
sample: Foo
In __exit__()

说明：
1. __enter__()方法被执行
2. __enter__()方法返回的值 - 这个例子中是"Foo"，赋值给变量'sample'
3. 执行代码块，打印变量"sample"的值为 "Foo"
4. __exit__()方法被调用

example4:
class Sample:
    def __enter__(self):
        return self

    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)

    def do_something(self):
        bar = 1/0
        return bar + 10

with Sample() as sample:
    sample.do_something()

输出结果：
type: <class 'ZeroDivisionError'>
value: division by zero
trace: <traceback object at 0x7f09f1af9788>
Traceback (most recent call last):
  File "exx.py", line 15, in <module>
    sample.do_something()
  File "exx.py", line 11, in do_something
    bar = 1/0
ZeroDivisionError: division by zero                             ##注意最后抛出了异常
#在with后面的代码块抛出任何异常时，__exit__()方法被执行。正如例子所示，异常抛出时，与之关联的type，value和stack trace传给__exit__()方法，
#因此抛出的ZeroDivisionError异常被打印出来了。
#先执行__enter__ 再执行具体的语句（在这里是do_something()),最后执行__exit__  。虽然do_something()报错，但是依然会执行__exit__()方法


example5:
with open("ex100.py") as file:
    print(file.readlines())

输出结果：FileNotFoundError: [Errno 2] No such file or directory: 'ex100.py'
###################################################################################################

######################assert()####################
assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达式为假。其返回值为假，就会触发异常
example1:
>>>assert 1 == 1
>>>assert 1 == 2
输出结果：AssertionError

assert断言语句添加异常参数，assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。
example2:
>>>assert 2==1,'what the fuck'
输出结果：AssertionError: what the fuck

example3:
>>> s = "nothin is impossible."
>>> key = "nothing"
>>> assert key in s, "Key: '{}' is not in Target: '{}'".format(key, s)
输出结果：
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AssertionError: Key: 'nothing' is not in Target: 'nothin is impossible.'
############################################################################################

###############break###################################################
break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。break语句用在while和for循环中。
break打破了最小封闭for或while循环。
example1:
for letter in 'Python':     # 第一个实例
    if letter == 'h':
        break
    print('当前字母 :', letter)

var = 10                    # 第二个实例
while var > 0:
   print('当前变量值 :', var)
   var = var -1
   if var == 5:   # 当变量 var 等于 5 时退出循环
      break

print("Good bye!")
输出结果：
当前字母 : P
当前字母 : y
当前字母 : t
当前变量值 : 10
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
Good bye!
#####################################################################

####################continue######################
Python continue 语句跳出本次循环，而break跳出整个循环。
continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。
continue语句用在while和for循环中。
example1:
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print('当前字母 :', letter)

var = 10                    # 第二个实例
while var > 0:
   var = var -1
   if var == 5:
      continue
   print '当前变量值 :', var
print "Good bye!"
输出结果：                                        #continue有一个删除的效果
当前字母 : P
当前字母 : y
当前字母 : t
当前字母 : o
当前字母 : n
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
当前变量值 : 4
当前变量值 : 3
当前变量值 : 2
当前变量值 : 1
当前变量值 : 0
Good bye!
#########################################################

##############################exception##############
 异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
一般情况下，在Python无法正常处理程序时就会发生一个异常。
异常是Python对象，表示一个错误。
当Python脚本发生异常时我们需要捕获处理它，否则程序会终止执行。
example1:
try:
    fh = open("testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:                                               #IOError:python的标准异常，为输入/输出操作失败
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fh.close()
输出结果：
内容写入文件成功
example2:
#在执行example11时，先在终端值执行，去掉testfile.txt的写权限
chmod -w testfile.txt
执行example1
输出结果：Error: 没有找到文件或读取文件失败
example3:
def temp_convert(var):
    try:
        return int(var)
    except ValueError:
        print("参数没有包含数字")

#调用函数
temp_convert("xyz");
输出结果：
参数没有包含数字
####################################################

###################finally#################
#finally,无论是否发生异常，都会运行finaaly
example1:
try:
    fh = open("testfile1", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
finally:
    print("无论try的block异常与否，都会打印此条")
输出结果：
无论try的block异常与否，都会打印此条
############################################################

###############################raise########################
我们可以使用raise语句自己触发异常
example1:
class ShortInputException(Exception):
    '''自定义异常类'''
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

try:
    s = input('please input:')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
except ShortInputException as e:
    print('输入长度是%s,长度至少是%s' %(e.length, e.atleast))
else:
    print('nothing...')


please input:hi
输出结果：
输入长度是2,长度至少是3

example2:
def try_exception(num):
  try:
    return int(num)
  except ValueError as e:
    print(e,"is not a number")
  else:
    print("this is a number inputs")

try_exception('xxx')
输出结果：
invalid literal for int() with base 10: 'xxx' is not a number

##############################################################

################exec##############
exec 执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。
example1:
>>>exec("print ('runoob.com')")
runoob.com

example2:
x= """
for i in range(5):
    print ("iter time: %d" % i)
 """
exec(x)
输出结果：
iter time: 0
iter time: 1
iter time: 2
iter time: 3
iter time: 4
############################################

#################is##############
is类似于==
>>>1 == 1
True
>>>1 is 1
True
#######################################

#########################pass#################
pass 是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句。
example1:
for letter in 'Python':
   if letter == 'h':
      pass
      print('这是 pass 块')
   print('当前字母 :', letter)
print "Good bye!"
输出结果：
当前字母 : P
当前字母 : y
当前字母 : t
这是 pass 块
当前字母 : h
当前字母 : o
当前字母 : n
Good bye!

example2:
def sample(n_samples):
    pass                          ####若函数为空会报错.pass占据一个位置
#######################################################################

####################斐波拉切数列yield说明###################################
example1:
def fab(max):                                  #制作斐波那契數列，max为生成个数
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b                         #注意写成a=b
        n = n + 1                               #       b=a+b   区别
fab(5)
输出结果：
1
1
2
3
5

example2:
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b      # 使用 yield
        #print(b)           #下次迭代时，代码从 yield b 的下一条语句继续执行,此时b变量仍为1,1,2,3,5
        a, b = b, a + b
        n = n + 1

for n in fab(5):                      #这里的for循环相当于next()
    print(n)

输出结果：
1
1
2
3
5

分析：1.简单地讲，yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable 对象！
在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
2.也可以手动调用 fab(5) 的 next() 方法（因为 fab(5) 是一个 generator 对象，该对象具有 next() 方法），这样我们就可以更清楚地看到 fab 的执行流程：见example3


example3:
>>>f = fab(5)
>>> f.next()
1
>>> f.next()
1
>>> f.next()
2
>>> f.next()
3
>>> f.next()
5
>>> f.next()
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
StopIteration



######################################################








##############next()#########################
返回迭代器的下一个项目。
next(iterator[, default])
iterator -- 可迭代对象
default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。

example1:
首先建立一个runoob.txt内容如下：
这是第一行
这是第二行
这是第三行
这是第四行
这是第五行

fo = open("runoob.txt", "r",encoding="utf-8")            #fo是一个可迭代对象(iterator)
print ("文件名为: ", fo.name)
for index in range(5):                                          ##试试range(6)会怎么样，输出结果StopIteration
    line = next(fo)  #python2中是line = fo.next()
    print ("第 %d 行 - %s" % (index, line))
# 关闭文件
fo.close()

输出结果：
文件名为:  runoob.txt
第 0 行 - 这是第一行

第 1 行 - 这是第二行

第 2 行 - 这是第三行

第 3 行 - 这是第四行

第 4 行 - 这是第五行

example2:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:                       #在遇到StopIteration时，捕获这个错误，先打印haha，再break
        # 遇到StopIteration就退出循环
        print("haha")                           #注意这里是会引发StopIteration
        break
输出结果：
1
2
3
4
5
hahh

example3:
it = iter([1, 2, 5, 4, 3])
while True:
    x = next(it, 'a')                        #如果传入第二个参数, 获取最后一个元素之后, 下一次next返回该默认值, 而不会抛出 StopIteration:
    print(x)
    if x == 'a':
        break

输出结果：
1
2
5
4
3
a

########################yield########################
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))

输出结果：
starting...
4
********************
res: None
4

注0. 如果你还没有对yield有个初步分认识，那么你先把yield看做“return”，这个是直观的，它首先是个return，普通的return是什么意思，就是在程序中返回某个值，
返回之后程序就不再往下运行了。看做return之后再把它看做一个是生成器（generator）的一部分（带yield的函数才是真正的迭代器）
1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个迭代对象)
2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成，所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，
4.程序执行print("*"*20)，输出20个*
5.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,
6.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4.

example2:
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))

输出结果：
starting...
4
********************
res: 7
4

注：
1.程序执行g.send(7)，程序会从yield关键字那一行继续向下运行，send会把7这个值赋值给res变量,从475行开始，但只有res =     没有yield 4
2.由于send方法中包含next()方法，所以程序会继续向下运行执行print方法，然后再次进入while循环
3.程序执行再次遇到yield关键字，yield会返回后面的值后，程序再次暂停，直到再次调用next方法或send方法。


example3:                                         #yield组合成生成器进行实现，占用内存少
def foo(num):
    print("starting...")
    while num<10:
        num=num+1
        yield num
for n in foo(0):
    print(n)


输出结果：
starting...
1
2
3
4
5
6
7
8
9
10


###################老式字符串格式####################
转义符                        描述                             示例
%d                         十进制整数                     "%d" % 45 == '45'
%i                         和%d一样                      "%i" % 45 == '45'
%o                         八进制数                      "%o" % 1000 == '1750'
%u                         无符号整数                    "%u" % -1000 == '-1000'
%x                         小写十六进制数                 "%x" % 1000 == '3e8'
%X                         大写十六进制数                 "%X" % 1000 == '3E8'
%e                         指数表示,小写e                 "%e" % 1000 =='1.000000e+03'
%E                         指数表示,大写e                 "%e" % 1000 =='1.000000E+03'
%f                         浮点实数                      "%f" % 10.34 == '10.340000'
%F                         浮点实数                      "%F" % 10.34 == '10.340000'
%g                         %f 和 %e 中较短的一种          "%g" % 10.34 == '10.34'
%G                         和%G一样                      "%G" % 10.34 == '10.34'
%c                         格式化字符及其ASCII码           "%c" % 34 == '"'
%r                         Repr格式                      "%r" % int == '<type 'int'>'
%s                         字符串格式                     "%s there" % 'hi' == 'hi there'
%%                         百分号自身                     "%g%%" % 10.34 == '10.34%'
####################################################################################


##############运算符#####################################
**                 幂
//                除后向下取整                2//4 = 0
%                 求余数                     2 % 4 = 2
{}                花括号                    {'x':5,'y':10}
@                 修饰器符                   @classmethod
;                                       print('hi');print('world')
+=                                      x=1; x += 2
-=
*=                                      x=1; x *= 2
/=
//=             除后舍余并赋值
%=              求余后赋值
**=             求幂后赋值
