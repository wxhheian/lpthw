the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"this is count {number}")

#same as above
for fruit in fruits:
    print(f"a fruit of type:{fruit}")

for i in change:
    print(f"i got {i}")

elements = []                                    #初始空list

for i in range(0,6):
    print(f"adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

for i in elements:
    print(f"element was: {i}")





##############append()###########
#  append() 方法用于在列表末尾添加新的对象。
#  >>>aList = [123, 'xyz', 'zara', 'abc'];
# >>>aList.append( 2009 );
# >>>print "Updated List : ", aList;
# Updated List :  [123, 'xyz', 'zara', 'abc', 2009]
###################################

#########range()###############
# range()函数用来创建一个整数列表
# range(start,stop,step)
# start:计数从start开始，默认是0
# stop:计数到stop结束，但不包括stop  eg. range(0,5)=[0,1,2,3,4]
# step:默认步长为1
# >>>range(10)
# [0，1，2，3，4，5，6，7，8，9]
# >>>range(1,11)
# [1,2,3,4,5,6,7,8,9,10]
# >>>range(0,30,5)
# [0,5,10,15,20,25]
# >>>range(0,-10,-1)
# [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
# >>>range(0)
# []
# >>>type(range(10))             #range返回对象是一个整数序列对象，而非list
# <class 'range'>
#>>> list(range(10))                #可以利用list返回列表
# [0,1,2,3,4,5,6,7,8,9]
>>>x=[[1,2,3],[4,5,6]]       #创建二维列表
##########################################
