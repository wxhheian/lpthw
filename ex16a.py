#truncate()方法用于截断文件，如果指定了可选参数size,则表示截断文件为size个字符。如果没有指定size，则从当前位置截断，截断之后的所有字符串被删除
fo = open("runoob.txt","r+")
print("文件名为：",fo.name)
line = fo.readline()         #readline()有定位的作用
print("读取第一行:%s" % line)

fo.truncate()

line = fo.readline()
print("读取数据：%s" % line)

fo.close()

##输出结果
文件名为： runoob.txt
读取第一行:这是第一行

读取数据：这是第二行
