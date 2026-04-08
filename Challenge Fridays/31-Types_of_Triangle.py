s1 = int(input("Enter the length of the first side: "))
s2 = int(input("Enter the length of the second side: "))
s3 = int(input("Enter the length of the third side: "))

unique_sides = len({s1, s2, s3})

if unique_sides == 1:
    print("The triangle is equilateral.")
elif unique_sides == 2:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
