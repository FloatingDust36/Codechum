n = int(input("Enter the value of N: "))
print(f"Enter {n} integers:")

nums = [int(input()) for _ in range(n)]

original = int(input("Enter the value of original: "))

while original in nums:
    original *= 2

print(f"Final value of original: {original}")
