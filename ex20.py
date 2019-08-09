from sys import argv

script, input_file = argv

def print_all(f):                              #这里定义f是一个file object
    print(f.read())                             #read（）读取文件

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    #print(line_count,f.readline(),end='')           #思考输出结果为为什么多出一个空行,因为readline()读取的内容中有本身就包含\n   end='' 的作用
    print(line_count,f.readline())                   #文件f会记录每次调用readline()后读取的位置，下次调用readline就读取接下来的一行
                                                     #readline()直到找到一个\n为止，然后停止读取文件
current_file = open(input_file)

print("first let's print the whole file:\n")                #\n打印之后隔行

print_all(current_file)

print("now let's rewind,kind of like a tape")             ##注意把20、22行代码注销掉，看看输出结果。注意seek(0)的作用:回到文件开始

rewind(current_file)

print("let's print three lines")

current_line=1
print_a_line(current_line,current_file)         #注意输出结果 1 this is line one

current_line=current_line+1
print_a_line(current_line,current_file)

current_line=current_line+1
print_a_line(current_line,current_file)


#  $print(3.6,"ddd")
#  输出结果   3.6 ddd
#  x += y     x = x + y
