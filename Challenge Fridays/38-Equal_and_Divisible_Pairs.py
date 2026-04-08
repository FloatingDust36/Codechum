n = int(input("Enter the number of integers (N): "))
print(f"Enter {n} integers:")

# Quickly build the array using a simple list comprehension
nums = [int(input()) for _ in range(n)]

k = int(input("Enter the integer K: "))

count = 0
for i in range(n):
    for j in range(i + 1, n):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1

print(f"Number of valid pairs: {count}")
