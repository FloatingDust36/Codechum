from itertools import accumulate

n = int(input("Enter the number of integers N: "))
print(f"Enter {n} integers:")

arr = [int(input()) for _ in range(n)]

print("Running sums are:")
print(" ".join(map(str, accumulate(arr))))
