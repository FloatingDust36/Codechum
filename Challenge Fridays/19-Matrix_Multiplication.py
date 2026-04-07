while True:
    a, b = map(int, input(
        "Enter matrix 1's number of rows and columns: ").split())
    c, d = map(int, input(
        "Enter matrix 2's number of rows and columns: ").split())
    if b == c:
        break
    print("Invalid dimensions")

print("Matrix 1")
m1 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(a)]

print("Matrix 2")
m2 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(c)]

print("Matrix Product:")
m2_cols = list(zip(*m2))

for row in m1:
    row_result = []

    # 2. Iterate through our newly transposed columns
    for col in m2_cols:
        # 3. Pair up the row and column elements, multiply, and sum instantly
        dot_product = sum(x * y for x, y in zip(row, col))
        row_result.append(dot_product)

    # 4. Print the finished row safely
    print(*row_result)


########################

while True:
    a, b = map(int, input(
        "Enter matrix 1's number of rows and columns: ").split())
    c, d = map(int, input(
        "Enter matrix 2's number of rows and columns: ").split())
    if b == c:
        break
    print("Invalid dimensions")

print("Matrix 1")
m1 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(a)]

print("Matrix 2")
m2 = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(c)]

print("Matrix Product:")
for i in range(a):
    row_result = []
    for j in range(d):
        dot_product = 0
        for k in range(b):
            # Multiply the k-th element of the row by the k-th element of the column
            dot_product += m1[i][k] * m2[k][j]
        row_result.append(dot_product)

    # Print the finished row separated by spaces
    print(*row_result)
