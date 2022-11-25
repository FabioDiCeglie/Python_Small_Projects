class Animal:
    def __init__(self,bread,color,weight):
        self.bread = bread
        self.color = color
        self.weight = weight

    def walk(self):
        print("I am walking")

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

class Dog(Animal):
    def bark(self):
        print("I am barking")


class Cat(Animal):
    def meow(self):
        print("I am meowing")

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

print(Derived.mro())
# [<class '__main__.Derived'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]
