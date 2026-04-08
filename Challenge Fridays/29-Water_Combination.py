# Grab dimensions
r, c = map(int, input("Enter houses rows and columns: ").split())
print("HOUSE:")

grid = []
for i in range(r):
    row_input = input(f"Row {i+1}: ").split()
    grid.append(row_input)

sources = set(input("Contamination Sources: ").split())

# 2. Locate all contaminated rows and columns
bad_r = set()
bad_c = set()
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if val in sources:
            bad_r.add(i)
            bad_c.add(j)

safe = []
for i, row in enumerate(grid):
    for j, val in enumerate(row):
        if i not in bad_r and j not in bad_c:
            safe.append(val)

if not safe:
    print("All houses contaminated")
elif len(safe) == r * c:
    print("All houses are safe")
else:
    print(f"Uncontaminated Houses = {' '.join(safe)}")
