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

    def eat(self):
        print("I am eating like a dog, messy!")


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

print(Derived.mro())
# [<class '__main__.Derived'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]


# POLYMORPHISM = take multiple forms
def make_animal_eat(animal):
    animal.eat()

blue_cat = Cat("british shorthair", "blue", 7000)
golden_dog = Dog("golden retriever", "golden", 5000)

make_animal_eat(blue_cat)
make_animal_eat(golden_dog)
