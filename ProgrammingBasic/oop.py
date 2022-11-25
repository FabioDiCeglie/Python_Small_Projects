# Fuctional programming
def computer_square_area(side_length):
    return pow(side_length, 2)

# OOP
class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def compute_area(self):
        return pow(self.side_length, 2)
