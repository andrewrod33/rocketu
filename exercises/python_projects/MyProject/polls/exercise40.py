class Song(object):

    def __init__(self,lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    def song_ish(self):
        for line in self.lyrics:
            print line

    def foo_bar(self):
        print "Let's do this"


happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song({"They rally around the family",
                        "With pockets full of shells"})
tupac = Song({"Gotta keep your head up",
              "To live in die in LA"})

happy_bday.sing_me_a_song()

happy_bday.song_ish()

bulls_on_parade.song_ish()

happy_bday.foo_bar()

tupac.song_ish()

