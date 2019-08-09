def add(a,b):
    print(f"adding {a} + {b}")
    return a + b                                             #return必须是函数的返回值  也就是说return只能存在与函数的定义中

def subtract(a,b):
    print(f"substracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"mutiplying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"dividing {a} / {b}")
    return a / b

print("let's do some math with just function!")

# age=add(int(input()),int(input()))                       #自己输入数字
# age=add(float(input()),float(input()))
age=add(30,5)                                 #return a+b的值赋给了age
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)

print(f"age: {age}, height：{height}, weight: {weight}, iq: {iq}")

#a puzzle for the extra credit ,type it in anyway
print("here is a puzzle")

what=add(age,subtract(height,multiply(weight,divide(iq,2))))                  #注意输出结果的由内向外打印

print("that becomes:",what,"can you do it by hand?")
