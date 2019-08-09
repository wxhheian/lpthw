from sys import argv
from os.path import exists                                    #参见pydoc os

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line,how?
in_file=open(from_file)
indata = in_file.read()                                             #读取文件内容并把它赋予给变量indata
#indata=open(from_file).read()                      #执行这个语句而注销9、10行  则无需运行in_file.close  因为read()一旦运行就会被关掉

print(f"the input file is {len(indata)} bytes long")                       #len()  返回对象（字符串、列表、元组）长度或个数

print(f"does the output file exist? {exists(to_file)}")                 #exists()  将文件名作为参数，如果文件存在，返回True;文件不存在，返回False
print("ready,hit return to continue, ctrl-c to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)                                       #把indata写入out_file中

print("alright,all done.")

out_file.close
in_file.close


#首先需要制作from_file  在终端执行代码  $echo "this is a test fie." >test1.txt
#                                   $cat test1.txt
#  用echo创建了文件，又用cat显示了文件
#  $man cat    #查询cat用法
