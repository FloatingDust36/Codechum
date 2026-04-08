# Parse inputs exactly matching the problem's string prompts
n = int(input("Enter the number of elements (N): "))
arr = list(
    map(int, input(f"Enter {n} integers in strictly increasing order: ").split()))
k = int(input("Enter K: "))

ans = k
for x in arr:
    if x <= ans:
        ans += 1
    else:
        break

print(f"The {k}-th missing positive integer is {ans}")
