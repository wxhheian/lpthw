from sys import argv          #   sys是一个模块(或者叫做库)  可查阅pydoc sys   argv:argument variable参数对象  sys中的一个object
# from sys import path
#read the WYSS section for how to run this
script, first, second, third = argv            #$把argv中的东西取出来，解包，将所有这些参数赋予左边这些变量 默认argv[0]=script pathname
# pathname =path

print("the script is called:",script)
print("your first variable is:",first)
print("your second variable is:",second)
print("your third variable is:",third)

# print("your script location is:",pathname)
#在终端上运行代码  $python3.6 ex13.py first 2nd 3nd
#argv  参数是在用户执行命令是输入
#input  参数是在脚本运行过程中输入
