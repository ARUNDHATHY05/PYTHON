class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

# User input for the first rectangle
length1 = float(input("Enter length of the first rectangle: "))
width1 = float(input("Enter width of the first rectangle: "))
rectangle1 = Rectangle(length1, width1)

# User input for the second rectangle
length2 = float(input("Enter length of the second rectangle: "))
width2 = float(input("Enter width of the second rectangle: "))
rectangle2 = Rectangle(length2, width2)

# Displaying the area of both rectangles
print(f"Area of rectangle 1: {rectangle1.area()}")
print(f"Area of rectangle 2: {rectangle2.area()}")

# Comparing the rectangles based on area
if rectangle1 < rectangle2:
    print("Area of rectangle 1 is smaller than rectangle 2.")
elif rectangle1 > rectangle2:
    print("Area of rectangle 1 is larger than rectangle 2.")
else:
    print("Area of rectangle 1 is equal to rectangle 2.")
