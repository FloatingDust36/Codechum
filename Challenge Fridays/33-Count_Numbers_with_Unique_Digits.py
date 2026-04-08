n = int(input("Enter an integer n: "))

# 1-DIGIT NUMBERS
# There are exactly 10 single-digit numbers (0 through 9). All of them are unique.
# If n=0, the only valid number is 0 (count is 1).
# If n>0, we start our grand total ('ans') at 10.
ans = 10 if n > 0 else 1

# 2-DIGIT NUMBERS (The Setup)
# To make a unique 2-digit number, the FIRST digit has 9 options (1-9).
# It cannot be 0, otherwise it becomes a 1-digit number.
# We store this starting pool of 9 choices in 'c'.
c = 9

# THE MATH LOOP (3-Digit, 4-Digit, etc.)
# We use a loop to calculate combinations for the remaining digits.
# 'i' represents the number of choices left for the CURRENT digit being added.
#
# For the SECOND digit: It has 9 options (0-9, but it cannot match the 1st digit).
# For the THIRD digit: It has 8 options (0-9, but cannot match the 1st or 2nd).
# This is why the range starts at 9 and steps down by -1.
for i in range(9, 10 - n, -1):

    # Calculate combinations for this specific length.
    # E.g., for 2 digits: 9 (first digit) * 9 (second digit) = 81 new numbers.
    # E.g., for 3 digits: 81 (previous digits) * 8 (third digit) = 648 new numbers.
    c *= i

    # Add the newly found unique numbers to our grand total.
    ans += c

print(f"Count of numbers with unique digits from 0 to {10**n - 1}: {ans}")
