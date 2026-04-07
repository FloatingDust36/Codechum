from itertools import combinations

n = int(input("Enter num: "))
items = [input(f"Item {i+1}: ") for i in range(n)]

for i in range(n + 1):
    for c in combinations(items, i):
        print(" ".join(c))
