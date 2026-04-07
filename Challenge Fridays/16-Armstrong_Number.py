n = input("Enter num: ")

sum = 0
for d in n:
    sum += int(d) ** len(n)

print(f"{n} is an Armstrong Number" if sum == int(
    n) else f"{n} is not an Armstrong Number")
