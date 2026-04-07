n = int(input("Enter number: "))
w = n if n % 2 else n - 1

for i in range(1, 2 * n):
    d = abs(n - i)
    print(("*" if d <= w // 2 else " ") * (2 * n) + "*" * (n - d))
