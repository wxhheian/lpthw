def break_words(stuff):
    """this function will break up words for us."""                     ##“”“”放在定义函数里相当于注释  在python环境下运行help(ex25)   help(ex25.break_words)  (先要import ex25)
    words = stuff.split(' ')                                             #以空格为分割符   split()返回的是一个list
    return words                                                         #return words 是一个虚拟变量  即如果不再python将stuff.split(' ')赋给words,则在运行第8行代码会出错

def sort_words(words):
    """sorts the words."""
    return sorted(words)                           #不像第3、4行代码，先将结果赋给一个变量，再return  #按字母顺序进行排序

def print_first_word(words):
    """prints the first word after popping it off."""
    word = words.pop(0)                                       #将list中的第一个弹出，并且保存在word变量中
    print(word)

def print_last_word(words):
    """prints the last word after popping it off."""
    word = words.pop(-1)                                #弹出最后一个元素
    print(word)

def sort_sentence(sentence):
    """takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


#####python环境下运行以下代码
# import ex25                                                #from ex25 import *      from ex25 import break_words
# sentence="All good things come to those who wait"
# words = ex25.break_words(sentence)
# words                                                   #输出结果以list的形式返回
# sorted_words=ex25.sort_words(words)
# sorted_words
# ex25.print_first_word(words)
# ex25.print_last_word(words)
# words
# ex25.print_first_word(sorted_words)
# ex25.print_last_word(sorted_words)
# sorted_words
# sorted_words = ex25.sort_sentence(sentence)
# sorted_words
# ex25.print_first_and_last(sentence)
# ex25.print_first_and_last_sorted(sentence)
###############















#################split()#############
#split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串  split()返回的是一个list
# str.split(str="", num=string.count(str)).
#     str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
#     num -- 分割次数。默认为 -1, 即分隔所有。
#example:
# str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
# print str.split( );       # 以空格为分隔符，包含 \n
# print str.split(' ', 1 ); # 以空格为分隔符，分隔成两个              #number+1  注意‘ ’中间有一个空格
#输出结果  ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
#        ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
# txt = "Google#Runoob#Taobao#Facebook"
# # 第二个参数为 1，返回两个参数列表
# x = txt.split("#", 1)
# 输出结果     ['Google', 'Runoob#Taobao#Facebook']
########################################

##########lambda############
#lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
#lambda所表示的匿名函数的内容应该是很简单的，如果复杂的话，干脆就重新定义一个函数了，使用lambda就有点过于执拗了。
#lambda就是用来定义一个匿名函数的，如果还要给他绑定一个名字的话，就会显得有点画蛇添足，通常是直接使用lambda函数。如下所示：
#example:
# add = lambda x, y : x+y
# add(1,2)  # 结果为3
#example:
# list1 = [3,5,-4,-1,0,-2,-6]
# sorted(list1, key=lambda x: abs(x))
#example:
# def get_y(a,b):
#      return lambda x:ax+b
# y1 = get_y(1,1)
# y1(1) # 结果为2
##############################33

###########sorted#############
#sorted() 函数对所有可迭代的对象进行排序操作。
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
#example1:
#a = (5,7,6,3,4,1,2)
#b = sorted(a)       # 保留原列表
#输出结果
#a=[5, 7, 6, 3, 4, 1, 2]
#b=[1, 2, 3, 4, 5, 6, 7]              注意sorte返回的是list,a=(),返回b=[]
#example2:
#L=[('b',2),('a',1),('c',3),('d',4)]
#sorted(L, key=lambda x:x[1])               # 利用key    对于list来说，x[1]是第二项，比较数字 ，x[0]是第一项，比较字母
#输出结果
#[('a', 1), ('b', 2), ('c', 3), ('d', 4)]

#example3：
#students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
#sorted(students, key=lambda s: s[2])            # 按年龄排序
#输出结果
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#sorted(students, key=lambda s: s[2], reverse=True)       # 按降序            #reverse=False 按升序 reverse=True 按降序
#输出结果
#[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
#############################

############pop()############
# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# list1 = ['Google', 'Runoob', 'Taobao']
# list_pop=list1.pop(1)
# print "删除的项为 :", list_pop
# print "列表现在为 : ", list1
#输出结果：
# 删除的项为 : Runoob
# 列表现在为 :  ['Google', 'Taobao']
#######################################
