n = int(input("Enter a number: "))
h = n//2

for i in range(-h, h+1):
    spa = abs(i)
    ast = (h * 2 + 1) - (spa * 2)

    print(str(n).center(h * 2 + 1, "*") if i == 0 else " " * spa + "*" * ast)
