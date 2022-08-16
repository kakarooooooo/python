class Dog():
    def __init__(self,breed, name, spots):
        self.breed = breed
        self.name = name

        self.spots = spots
    def bark(self):
        print(f"BARKBARKBARKBARK {self.name}")

my_dog = Dog(breed = "Lab", name = "Sammy", spots = False)

# print(my_dog)
# my_dog.bark()

# your_dog = Dog("Lab","Sam",True)

class Circle():
    pass

class Animal():
    def __init__(self) :
        print("ANIMAL CREATED")
    def who_am_i(self):
        print ("I am an animal")
    def eat(self):
        print("I am eating")

myanimal = Animal()
myanimal.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

mydog = Dog()