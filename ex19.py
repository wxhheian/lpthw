def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have {cheese_count} cheese!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("get a blanket.\n")                                         #\n换行


print("we can just give the function numbers directly:")
cheese_and_crackers(20,30)


print("or,we can use variables from our scripts:")
amount_of_cheese = 10                                      #全局变量amount_of_cheese最好不要和函数变量名cheese_count取名一样
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can even do math inside too:")
cheese_and_crackers(10+20,5+6)



print("and we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)



##注意输出结果
