ten_things ="Apples Orange Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')                                   ##split结果是一个list
more_stuff = ["Day", "Night", "Song","Frisbee",
            "Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now.")

print("there we go:",stuff)

print("let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])                      #输出列表的最后一个元素
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))


###################join######################
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。str.join(元组、列表、字典、字符串) 之后生成的只能是字符串。
#example1:
#str = "-";
#seq = ("a", "b", "c"); # 字符串序列
#print str.join( seq );

#输出结果：
#a-b-c

#example2:
#seq = {'hello':'nihao','good':2,'boy':3,'doiido':4}
#print('-'.join(seq))        #字典只对键进行连接

#输出结果：
#hello-good-boy-doiido

#example3:   列表中的元素也需要是字符串：
#print(','.join(['1','2','3','4']))                          #print(''.join([1,2,3,4]))  程序报错

#输出结果：
#1，2，3，4
