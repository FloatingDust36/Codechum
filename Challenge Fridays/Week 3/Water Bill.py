let = input("Enter package: ")
num = int(input("Enter cubic meter used: "))

if let == 'A':
    res = 250 + 9.50 * num
if let == 'B':
    if num >= 20:
        res = 400 + 11.25 * (num-20)
    else:
        res = 400
if let == 'C':
    if num < 12:
        res = 300
    elif num <= 25:
        res = 525
    else:
        res = 750

print(f"Payment: {res:.2f}")
