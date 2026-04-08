start = int(input("Enter start: "))
end = int(input("Enter end: "))
divisor = int(input("Enter divisor: "))

count = 0

for i in range(start, end + 1):
    difference = abs(i - int(str(i)[::-1]))

    if difference % divisor == 0:
        count += 1

print(f"The number of just right numbers is: {count}")
