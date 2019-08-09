#formatter="{} {} {} {}"
formatter="{}\n{}\n{}\n{}"                     #比较第一行与第二行

print(formatter.format(1,2,3,4))                                # “1” 会出错
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))                   #思考为什么true不用打“”
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
        "try your",
        "own text here",
         "maybe a poem",
        "or a song about fear"
))                                                  #仍然打印在一行，注意美观
