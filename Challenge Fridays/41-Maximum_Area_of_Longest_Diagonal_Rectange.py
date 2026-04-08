n = int(input("Enter the number of rectangles: "))

max_d2 = 0
ans_area = 0

for i in range(1, n + 1):
    l, w = map(int, input(
        f"Enter length and width for rectangle {i}: ").split())

    d2 = l*l + w*w
    area = l*w

    if (d2, area) > (max_d2, ans_area):
        max_d2, ans_area = d2, area

print(f"The area of the rectangle with the longest diagonal is: {ans_area}")
