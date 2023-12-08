class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# User input for the first rectangle
length1 = float(input("Enter length of the first rectangle: "))
breadth1 = float(input("Enter breadth of the first rectangle: "))
rectangle1 = Rectangle(length1, breadth1)

# User input for the second rectangle
length2 = float(input("Enter length of the second rectangle: "))
breadth2 = float(input("Enter breadth of the second rectangle: "))
rectangle2 = Rectangle(length2, breadth2)

# Display area and perimeter for the first rectangle
print(f"\nArea of the first rectangle: {rectangle1.area()}")
print(f"Perimeter of the first rectangle: {rectangle1.perimeter()}")

# Display area and perimeter for the second rectangle
print(f"\nArea of the second rectangle: {rectangle2.area()}")
print(f"Perimeter of the second rectangle: {rectangle2.perimeter()}")

# Comparing rectangles based on area
if rectangle1.area() > rectangle2.area():
    print("\nThe first rectangle has a greater area.")
elif rectangle1.area() < rectangle2.area():
    print("\nThe second rectangle has a greater area.")
else:
    print("\nBoth rectangles have the same area.")
