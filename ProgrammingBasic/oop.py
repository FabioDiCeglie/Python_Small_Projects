# what is difference from a class or an object?

   # A class is a blueprint or a module from which we can create instances or object.

# Fuctional programming
def computer_square_area(side_length):
    return pow(side_length, 2)

# OOP
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

# if it is defined inside a class this is called methods
    def compute_area(self):
        return pow(self.side_length, 2)

example_square = Square(15)
print(example_square.compute_area())

small_square = Square(2)
print(small_square.compute_area())

big_square = Square(1000)
print(big_square.compute_area())
