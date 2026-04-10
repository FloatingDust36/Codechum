a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

print(f"Result: {eval(f'{a}{op}{b}'):.2f}")
