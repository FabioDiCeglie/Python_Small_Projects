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

