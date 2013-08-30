class Person(object):
    def __init__(self, name, sex, age):
        self.age = int(age)
        self.name = name
        self.sex = sex

    def who(self):
        print "Hello %s!" % self.name

    def birthday(self):
        self.age +=1

peep = Person("Andrew", "male", "111")

print peep.age

peep.who()



