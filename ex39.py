#######list替换####
# things= ['a','b','c','d']
# print(things[1])
# things[1] = 'z'
# print(things[1])
#
# ###dic替换,删除####
# stuff={'name':'zed','age':39,'height':6*12+2}
# print(stuff['name'])
# print(stuff['age'])
# stuff['city'] = "SF"
# print(stuff['city'])
# stuff
# stuff[1] = 'wow'
# stuff['2'] = 'neato'
# print(stuff['2'])
# del stuff['city']
# del stuff[1]
# del stuff['2']
# stuff

#####ex39.py###
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
    }
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
    }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-'*10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is:",states['Michigan'])
print("Forida's abbreviation is:", states['Florida'])

print('-' * 10)
print("Michigan has:", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

print('-' * 10)
for state, abbrev in list(states.items()):                         #states.items()与list(states.items())类型不同，前者是dict_items,后者是list
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
state = states.get('Texas')

if not state:
    print("sorry, no Texas.")

city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is:{city}")


###########################item()############################################
#字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。
#example1:
# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#
# print("字典值 : %s" %  dict.items())
#
# # 遍历字典列表
# for key,values in  dict.items():
#     print(key,values)

##输出结果##
# 字典值 : dict_items([('Google', 'www.google.com'), ('Runoob', 'www.runoob.com'), ('taobao', 'www.taobao.com')])
# Google www.google.com
# Runoob www.runoob.com
# taobao www.taobao.com
#############################################################################

######################__contains__##############################################
##字典（Dictionary）  __contains__(key)函数，用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回fals
#example1:
# dict3 = {'name':'z','Age':7,'class':'First'};
# print("Value : ",dict3.__contains__('name'))
# print("Value : ",dict3.__contains__('sex'))

#输出结果：
# Value :  True
# Value :  False
######################################################

##################元组################################################
#Python的元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
##################创建元组
# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5 )
# tup3 = "a", "b", "c", "d"
#创建空元组
#tup = ()
###############访问元组
#tup1[1]
############元组不能修改，但可以拼接
#tup1 = (12, 34.56)
#tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
# 创建一个新的元组
#tup3 = tup1 + tup2
#输出结果：
#(12, 34.56, 'abc', 'xyz')
#############元祖的删除，元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
#tup = ('physics', 'chemistry', 1997, 2000)
#print(tup)
#del tup
###############元组运算符
#len((1,2,3)) == 3
#(1, 2, 3) + (4, 5, 6) == (1,2,3,4,5,6)
#('Hi!',) * 4 == ('Hi!', 'Hi!', 'Hi!', 'Hi!')
#3 in (1, 2, 3) == True
#for x in (1, 2, 3): print x  == 1 2 3

###########################################################################

############dict.get()
# dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值值。
#example1:
# dict = {'Name': 'Zara', 'Age': 27}
# print "Value : %s" %  dict.get('Age')
# print "Value : %s" %  dict.get('Sex', "Never")
#输出结果：
# Value : 27
# Value : Never
###################################################################

########################collections.OrderedDict##############
##很多人认为python中的字典是无序的，因为它是按照hash来存储的，但是python中有个模块collections(英文，收集、集合)，里面自带了一个子类
#OrderedDict，实现了对字典对象中元素的排序。
# print('Regular dictionary:')
# d2={}
# d2['a']='A'
# d2['b']='B'
# d2['c']='C'
#
# d3={}
# d3['c']='C'
# d3['a']='A'
# d3['b']='B'
#
# print d2 == d3
#
# print('\nOrderedDict:')
# d4=collections.OrderedDict()
# d4['a']='A'
# d4['b']='B'
# d4['c']='C'
#
# d5=collections.OrderedDict()
# d5['c']='C'
# d5['a']='A'
# d5['b']='B'
#
# print(d1==d2)
#
# 输出：
# Regular dictionary:
# True
#
# OrderedDict:
# False
