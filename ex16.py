from sys import argv

script, filename = argv

print(f"we're going to erase {filename}.")
print("if you don't want that, hit CTRL-C (^C).")                #快捷键ctrl+c 强制结束进程
print("if you do want that, hit RETURN.")

input("?")

print("Opening the file ...")
target=open(filename, 'w')                        #open(filename)  默认‘r’模式  新建一个test.txt并且以write的模式
                                                  #若在当前目录下没有test.txt,则新建
print("truncating the file. goodbye!")
target.truncate()                                 #清空文件  若已存在test.txt则清空内容；若新建的test.txt,这条命令无用

print("now i'm going to ask you for three lines.")

line1=input("line1:")
line2=input("line2:")
line3=input("line3:")

print("i am going to write these to the file.")

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"{line1}\n{line2}\n{line3}")             #用格式化的字符串简写25-30行代码

print("and finally,we close it.")
target.truncate()             #光标已经在最后，所以这个truncate()实际没有作用
target.close()                 #关闭文件对象（file object）

#在终端运行代码
#$python3.6 ex16.py test.txt
#查阅函数 close  read  readline truncate  write  seek(0)
#文件打开模式 r  r+  w  w+ a  a+  rb rb+  wb wb+  ab  ab+
