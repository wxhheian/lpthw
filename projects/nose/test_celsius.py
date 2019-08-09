import nose
from temperature import *

def test_freezing():
    assert to_celsius(32) == 0

def test_boiling():
    assert to_celsius(212) == 100

def test_roundoff():
    assert to_celsius(100) == 38


#在终端输入
#$nosetest -v test_celsius.py

# 常用命令行参数：
#
#         a) -w ，指定一个目录运行测试。目录可以是相对路径或绝对路径。
# 
# 　　例如： nosetest -w c:\pythonTests\Test1，只运行目录c:\pythonTests\Test1下的测试。可以指定多个目录，例如： nosetest -wc:\pythonTests\Test1 -w c:\pythonTests\Test2。
#
#
#
# 　　b)-s，不捕获输出，会让你的程序里面的一些命令行上的输出显示出来。例如print所输出的内容。
#
#
#
# 　　c)-v，查看nose的运行信息和调试信息。例如会给出当前正在运行哪个测试。
