import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:                                               #if用来检验一个变量的真值，基于这一真值来决定是否运行代码。 当文件运行到结尾时，readline()会返回一个空字符串，为False
        print_line(line, encoding,errors)                  #if就是用来检查这个空字符串的，只要readline()返回了内容，这里就为真，便执行9～10行，否则9～10行跳过
        return main(language_file,encoding,errors)         #在函数里嵌套函数,if在这里的功能是防止循环永远下去


def print_line(line,encoding,errors):
    next_lang=line.strip()                                          #strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。把每行结尾的\n删掉
#    next_lang=line                                                 #若不加strip 打印时会换行
    raw_bytes=next_lang.encode(encoding,errors=errors)               #encode() 方法以 encoding 指定的编码格式编码字符串
    cooked_string=raw_bytes.decode(encoding,errors=errors)           #decode() 方法以 encoding 指定的编码格式解码字符串

    print(raw_bytes,"<===>", cooked_string)


languages=open("languages.txt",encoding="utf-8")

main(languages,encoding,error)



####################
#strip用法：用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
# str = "00000003210Runoob01230000000";
# print(str.strip( '0' ));  # 去除首尾字符
# str2 = "   Runoob      ";   # 去除首尾空格
# print(str2.strip());
#输出结果
#3210Runoob0123
#Runoob
####################

##############
# str = "this is string example....wow!!!";
# str = str.encode('base64','strict');
# print "Encoded String: " + str;
# print "Decoded String: " + str.decode('base64','strict')
# 输出结果
#Encoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=
#Decoded String: this is string example....wow!!!
######################
#百度ASCII: 将二进制、十进制、十六进制、各种字母符号一一对应 ； 不够 引入utf-8编码规则  ； unicode(universal encoding)编码规则
#了解encode Decode
#了解1或0bit(位)  1byte(字节)=8bit   字节序列

####在python中运行
#>>>raw_bytes=b'\xe6\x96\x87\xe8\xa8\x80'              #b''告诉python是原始字节序列
#>>>utf_string="文言”
#>>>raw_bytes.decode()
#>>>utf_string.encode()

#尝试其他编码方式
#$python3.6 ex23.py utf-16 strict
#$python3.6 ex23.py utf-32 strict
#$python3.6 ex23.py Big5 replace      #big5不能编码位置0的某些字符
