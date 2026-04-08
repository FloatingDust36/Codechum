x1 = int(input("Enter x of rectangle point 1: "))
y1 = int(input("Enter y of rectangle point 1: "))
x2 = int(input("Enter x of rectangle point 2: "))
y2 = int(input("Enter y of rectangle point 2: "))

# Calculate dimensions instantly using absolute value
width = abs(x1 - x2)
height = abs(y1 - y2)

print(f"\nPerimeter of the rectangle: {2 * (width + height)}")
print(f"Area of the rectangle: {width * height}")

###########


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return abs(self.p1.x - self.p2.x) * abs(self.p1.y - self.p2.y)

    def perimeter(self):
        return 2 * (abs(self.p1.x - self.p2.x) + abs(self.p1.y - self.p2.y))


# Input Phase
x1 = int(input("Enter x of rectangle point 1: "))
y1 = int(input("Enter y of rectangle point 1: "))
x2 = int(input("Enter x of rectangle point 2: "))
y2 = int(input("Enter y of rectangle point 2: "))

# Build the objects
rect = Rectangle(Point(x1, y1), Point(x2, y2))

# Output Phase
print(f"\nPerimeter of the rectangle: {rect.perimeter()}")
print(f"Area of the rectangle: {rect.area()}")
