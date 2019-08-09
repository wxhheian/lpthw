from sys import argv                       #从sys这个软件包中获得argv这个特性

script, filename = argv

txt =open(filename)                    #从open函数获得一个file文件，即txt是一个文件对象（file object),不是它的内容

print(f"here is your file {filename}：")
print(txt.read())
txt.close()                               #关闭txt文件对象
print("tpye the filename again:")
file_again = input(">")

txt_again=open(file_again)

print(txt_again.read())
txt_again.close()
