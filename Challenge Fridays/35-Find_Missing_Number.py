n = int(input("Enter the number of elements: "))
print(f"Enter {n} elements (between 1 and {n+1}):")

arr = list(map(int, input().split()))

expected_sum = (n + 1) * (n + 2) // 2

ans = expected_sum - sum(arr)

print(f"The missing number is: {ans}")
