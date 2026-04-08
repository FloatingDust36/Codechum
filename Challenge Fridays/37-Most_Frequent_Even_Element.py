n = int(input("Enter the number of integers: "))
print(f"Enter {n} integers:")

counts = {}

# Process and filter inputs on the fly
for _ in range(n):
    val = int(input())
    if val % 2 == 0:
        counts[val] = counts.get(val, 0) + 1

if not counts:
    print("Most Frequent Even Element: -1")
else:
    ans = max(counts, key=lambda k: (counts[k], -k))
    print(f"Most Frequent Even Element: {ans}")
