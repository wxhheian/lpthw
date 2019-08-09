class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["happy birthday to you",
                "i don't want to get sued",
                "so i'll stop right there"])                   #将类实例化为对象，并将该对象赋值给happy_bday这个变量

bulls_on_parade = Song(["they rally around the family",
                         "with pockets full of shells"])

happy_bday.sing_me_a_song()                       #调用对象的函数
bulls_on_parade.sing_me_a_song()
