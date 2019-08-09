people = 30
cars = 40
trucks = 15


if cars > people:
    print("we should take the cars.")
elif cars < people:                                             ##注意elif 与if 对齐
    print("we should not take the cars.")
else:                                                          ##else与if对齐
    print("we can'tdecide.")

if trucks > cars:
    print("that's too many trucks.")
elif trucks < cars:
    print("maybe we could take the trucks")
else:
    print("we still can't decide.")

if people > trucks:
    print("alright, let's just take the trucks.")
else:
    print("fine,let's stay home then.")


##如果多个elif块都是True ,python只会运行它运行的第一个True块
