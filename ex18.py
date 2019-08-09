#this one is like your scripts with argv
def print_two(*args):                 # *作用：把函数的所有参数都接收进来，然后放到名叫args的列表中去
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2:{arg2}")

#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):                          #与*args作用一样
    print(f"arg1: {arg1}, arg2:{arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no argument
def print_none():                              #函数可以不接收参数
    print("i got nothin'.")


print_two(222,333)                             #参数为数字不用加“”
#print_two("zed","shaw")                        #  不加“”会出错
print_two_again("zed","shaw")
print_one("first!")
print_none()


#函数命名由字母、数字、下划线组成，不能以数字开头
