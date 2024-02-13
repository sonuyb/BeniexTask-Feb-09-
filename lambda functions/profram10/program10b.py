from program10 import rectangle_area
def arearectangle(length,width):
    area = rectangle_area(length,width)
    return area
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
res = arearectangle(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {res}")