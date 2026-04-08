n = int(input("Enter an integer: "))

# A number only loses its original value upon double reversal if it has trailing zeros.
print(n == 0 or n % 10 != 0)
