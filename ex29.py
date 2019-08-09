people = 20
cats = 30
dogs = 15


if people < cats:                                            #if 返回True或False  为真则执行接下来的语句， 为假则跳过
    print("Too many cats! the world is doomed")

if people > cats:
    print("not many cats! the world is saved")

if people < dogs:
    print("the world is drooled on!")

if people > dogs:
    print("the world is dry")

dogs +=5                                       #  +=递增运算符  dog = dog + 5

if people > dogs:
    print("people are greater than or equal to dogs.")

if people < dogs:
    print("people are less than or equal to dogs.")

if people == dogs:
    print("people are dogs")

# if 1 == 1:
#     print("people are dogs")
