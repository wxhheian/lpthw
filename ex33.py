i = 0
numbers = []

while i < 6:
    print(f"at the top i is {i}.")
    numbers.append(i)

    i = i + 1
    print("numbers now:",numbers)
    print(f"at the bottom i is {i}")


print("the number:")

for num in numbers:
    print(num)



###ctrl+c  强制程序终止
##while循环
##while循环所作的与if语句类似，去检查一个布尔表达式的真假，但不是只执行一次，而是执行完后再跳到while顶部，如此重复直到False为止
