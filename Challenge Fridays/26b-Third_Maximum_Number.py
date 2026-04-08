n = int(input("Enter the number of integers: "))
print(f"Enter {n} integers:")

unique_nums = set()

for _ in range(n):
    val = int(input())
    unique_nums.add(val)

sorted_nums = sorted(list(unique_nums), reverse=True)

if len(sorted_nums) >= 3:
    ans = sorted_nums[2]
else:
    ans = sorted_nums[0]

print(f"The third distinct maximum number is {ans}")
