from sys import exit

def gold_room():                             #注意这个函数定义没有参数
    print("this room is full of gold. how much do you take?")

    choice = input(">")
    if "0" in choice or "1" in choice:                             ##若input输入为22 则会执行dead("man,learn...")
        how_much = int(choice)
    else:
        dead("man,learn to type a number")

    if how_much < 50:
        print("nice, you're not greedy,you win!")
        exit(0)
    else:
        dead("you greedy bastard!")


def bear_room():
    print("there is a bear here.")
    print("the bear has a bunch of honey")
    print("the fat bear is in front of another door.")
    print("how are you going to move tthe bear?")
    bear_moved = False

    while True:                                                      #表示无限循环
        choice = input(">")                                            ###input输入hahahha  则会执行else 并一直循环

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:                      ##注意逻辑的顺序 先choice == "taunt bear"
            print("the bear has moved from the door.")
            print("you can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("i got no idea what that means")

def cthulhu_room():
    print("here you see the great evil cthulhu.")
    print("he,it, whatever stares at you and you go insane.")
    print("do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:                                          ###input输入的内容为字符串  若choice= abcdfleegjkjk  执行start()
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print(why,"good job!")
    exit(0)                                                  #exit(0) 无错误退出  exit(1) 有错误退出

def start():
    print("you are in a dark room.")
    print("there is a door to your right and left.")
    print("which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice =="right":
        cthulhu_room()
    else:
        dead("you stumble around the room until you starve.")


start()
