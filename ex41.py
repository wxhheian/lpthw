import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES ={
    "class %%%(%%%):":
    "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
    "Set *** to an instance of class %%%.",
    "***.***(@@@)":
    "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
    "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))           ##返回对象的str格式  注意type(word) == bytes

#print(WORDS)                   #WORDS是个list,每个元素是个字符串

def convert(snippet,phrase):
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]    #将随机抽到的一个或两个WORDS首字母大写
    other_names = random.sample(WORDS,snippet.count("***"))
    results = []
    param_names = []

    for i in range(0,snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]                                   #result有两个结果

        #fake class class_names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other class_names
        for word in other_names:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

#keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input(">")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")


#######################################区别read readline readlines########################
# 假设a.txt的内容如下：
# Hello
# Welcome
# What is the fuck..

#example1:  read(size)从文件当前位置读取size个字节，若无参数，则读取全文
# f=open("a.txt")
# lines = f.read()
# print(lines)
# print(type(lines))
# f.close

# 输出结果：
# Hello
# Welcome
# What is the fuck..
# <type 'str'>

#example2: readline() 每次读取一行，该方法返回一个字符串对象
# f = open("a.txt")
# line = f.readline()
# print(type(line))
# while line:
#     print(line)
#     line = f.readline()
# f.close()

# 输出结果：
#     <type 'str'>
#     Hello
#     Welcome
#     What is the fuck...

#example3: readlines()读取文件的所有行，并保存在一个list,每一行作为一个元素
# f = open("a.txt")
# lines = f.readlines()
# print(type(lines))
# for line in lines:
#     print(line)
# f.close

#输出结果
    # <type 'list'>
    # Hello
    # Welcome
    # What is the fuck...
#############################################################################

#############random##################################
# random()方法返回随机生成的一个范围在（0，1）的实数
# random()不能直接访问，需要导入random模块
#example1:
# import random
# random.random()        #生成一个范围在（0，1）之间随机数,
# random.randint(1,10)     #生成1到10之间的一个整数型随机数
# random.uniform(1.1,5.4)   #生成1.1到5.4之间的随机浮点数
# random.choice('tomorrow')  #从序列中随机选取一个元素
# random.randrange(1,100,2)   #生成从1到100的间隔为2的随机整数
# a=[1,3,4,5,7]
# random.shuffle(a)       #将List中的元素打乱
# print(a)
#list=[1,2,3,4,5,6,7,8,9,10]
#slice = random.sample(list,5)   #从list中随机获取5个元素
#print(slice)
###########################################################

###################str.count####################
#example1:
# count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# str = "this is string example....wow!!!";
# sub = "i";
# print "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)
# sub = "wow";
# print "str.count(sub) : ", str.count(sub)
# #输出结果：
# str.count(sub, 4, 40) :  2
# str.count(sub) :  1
############################################################

##############replace()######################################
#replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
#str.replace(old, new[, max])
# str = "this is string example....wow!!! this is really string";
# print str.replace("is", "was");
# print str.replace("is", "was", 3);
#
# 输出结果：
# thwas was string example....wow!!! thwas was really string
# thwas was string example....wow!!! thwas is really string
