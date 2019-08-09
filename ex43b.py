#在很多类型的操作系统里，exit(0) 可以中断某个程序，而其中的数字参数则用来表示程序是否是碰到错误而中断。exit(1) 表示发生了错误，而 exit(0) 则表示程序是正常退出的
#不过你可以用不一样的数字表示不同的错误结果。比如你可以用exit(100) 来表示另一种和 exit(2)或 exit(1) 不同的错误。
#os._exit()会直接将python程序终止，之后的所有代码都不会继续执行。
#sys.exit()会引发一个异常：SystemExit，如果这个异常没有被捕获，那么python解释器将会退出。如果有捕获此异常的代码，那么这些代码还是会执行
from sys import exit
import os
try:
    sys.exit(0)
except:
    print('die')
finally:
    print('clean up')

try:
    os._exit(0)
except:
    print('die')
print('os.exit')  #不打印直接退出了
