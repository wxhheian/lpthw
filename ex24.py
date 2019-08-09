print("let's pracice everything.")
print('you\'d need to know \'bout escapes with \\ that do: ')
print('\n newlines and \t tabs.')                                   #注意\n 与 newlines 中间多了个空格注意输出结果也有一个空格
                                                                    #注意and tabs 中间的\t也有空格，注意输出结果
poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of lovel
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is noneself.
"""
                                                                  #“”“”有\n的作用(上下都换行)
print("---------------")
print(poem)
print("-----------------")

five =10-2+3-6
print(f"this should be five:{five}")

def secret_formula(started):
     jelly_beans = started * 500
     jars = jelly_beans / 1000
     crates = jars / 100
     return jelly_beans, jars, crates

start_point= 10000
beans, jars, crates =secret_formula(start_point)          #记住函数内部的变量都四临时的，将函数内部的变量jelly_beans赋予给了beans


#remember that this is another way to format a string
print("with a starting point of: {}".format(start_point))
#it just like with an f"" String
print(f"we'd have {beans} beans,{jars} jars, and {crates} crates.")

start_point=start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)                         #与28行代码作比较
print("we'd have {} beans, {} jars, and {} crates.".format(*formula))
