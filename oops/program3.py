class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return self.side_length * 2

square1 = Square(5)
print("Area of the square:", square1.area())
print("Perimeter of the square:", square1.perimeter())