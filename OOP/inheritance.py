from abc import ABC, abstractmethod



class Animal(ABC):
    def __init__(self,breed,color,weight):
        self.breed = breed
        self.color = color
        self.weight = weight

    def walk(self):
        print("I am walking")

    @abstractmethod
    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Dog(Animal):
    def bark(self):
        print("I am barking")

    def eat(self):
        print("I am eating like a dog, messy!")

    def __eq__(self, other):
        return type(self) == type(other) and self.weight == other.weight

    def __ne__(self, other):
        return type(self) == type(other) and self.weight != other.weight

    def __str__(self):
        return f"I am a dog of {self.breed} breed, my fur color is {self.color} and I weigh {self.weight}!"


class Cat(Animal):
    def meow(self):
        print("I am meowing")

    def eat(self):
        print("I am eating like a cat")


class DetectDrugsMixin:
    def detect_drugs(self):
        print("I am detecting some drugs here!")


class PoliceDog(Dog, DetectDrugsMixin):
    def __init__(self, breed, color, weight, hours_on_mission):
        super().__init__(breed, color, weight) #it call the superclass Dog
        self.hours_on_mission = hours_on_mission

    # def detect_drugs(self):
    #     print("Sniff .. sniff .. I smell some weed here!")

class Base1:
    x = "base1"


class Base2:
    x = "base2"


class Derived(Base1, Base2):
    pass

# airport_dog = PoliceDog("german", "golden", 5000, 100)
# print(airport_dog.detect_drugs())

# print(Derived.mro())
# [<class '__main__.Derived'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]


# POLYMORPHISM = take multiple forms

# def make_animal_eat(animal):
#     animal.eat()

# blue_cat = Cat("british shorthair", "blue", 7000)
# golden_dog = Dog("golden retriever", "golden", 5000)

# make_animal_eat(blue_cat)
# make_animal_eat(golden_dog)

# MAGIC METHODS
blue_cat = Cat("british shorthair", "blue", 7000)
golden_dog = Dog("golden retriever", "golden", 5000)
french = Dog("french bulldog", "brown", 2000)
golden_dog2 = Dog("golden retriever", "golden", 2000)

# print(golden_dog == french) # for comparing we need the magic methods
# print(french == golden_dog2)
# print(french != golden_dog2)
# print(golden_dog2 == blue_cat)
# print(golden_dog2)


# Most frequently used magic methods:
# Addition (+): __add__(self, other)
# Subtraction (-): __sub__(self, other)
# Multiplication (*): __mul__(self, other)
# Floor division (//): __floordiv__(self, other)
# True division (/): __truediv__(self, other)
# Modulo (%): __mod__(self, other)
# Power (**): __pow__(self, other)
# Less than (<): __lt__(self, other)
# Greater than (>): __gt__(self, other)
# Less than or equal (<=): __le__(self, other)
# Greater than or equal(>=): __ge__(self, other)
# Equals (==): __eq__(self, other)
# Not equals (!=): __ne__(self, other)

# ABSTRACTION

french.eat()
blue_cat.eat()


class IEmail(ABC):
    @abstractmethod
    def send(self):
        pass

    @property
    @abstractmethod
    def valid_domain(self):
        pass


class Email(IEmail):
    valid_domain = "epicpython.io"

    def send(self):
        print(f"Sending and email from the email class with the valid domain {self.valid_domain}")


email = Email()
email.send()
