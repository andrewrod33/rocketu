class Animal(object):
    pass

## Do is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a name
        self.name = name

        ##Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        ##Employee has-a name and salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is a fish
class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

##Cat has-a name
satan = Cat("Satan")

##Mary has-a name
mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()


