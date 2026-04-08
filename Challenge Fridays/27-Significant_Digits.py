import math

n1, op, n2 = input("Enter operation: ").split()
ans = eval(f"{n1} {op} {n2}")

if op in '+-':
    # Count decimal places:
    # If a '.' exists, split the string and count the characters on the right side.
    # If no '.' exists, default to 0 decimal places.
    dec1 = len(n1.split('.')[1]) if '.' in n1 else 0
    dec2 = len(n2.split('.')[1]) if '.' in n2 else 0

    print(f"Answer: {ans:.{min(dec1, dec2)}f}")
else:
    # Count significant figures:
    # lstrip('-') removes negatives so they don't count towards the digit length.
    # If '.' exists: trailing zeros matter! Remove the dot and leading zeros, count the rest.
    # If no '.' exists: trailing zeros do NOT matter! Strip zeros from both sides, count the rest.
    sf1 = len(n1.lstrip('-').replace('.', '').lstrip('0')
              ) if '.' in n1 else len(n1.lstrip('-').strip('0'))
    sf2 = len(n2.lstrip('-').replace('.', '').lstrip('0')
              ) if '.' in n2 else len(n2.lstrip('-').strip('0'))

    # Determine the target significant figures.
    # The "or 1" handles edge cases where stripping all zeros leaves an empty string (like input "0").
    figs = min(sf1 or 1, sf2 or 1)

    # math.log10(0) throws a ValueError, so we instantly catch an answer of 0.
    if ans == 0:
        print("Answer: 0")
    else:
        # Calculate rounding position relative to the decimal:
        # math.log10(abs(ans)) -> Finds the scientific magnitude of the answer.
        # floor() -> Drops decimals from the magnitude.
        # ans = 45600 ➔ 4.56 * 10^4 ➔ Magnitude = 4
        # ans = 0.0456 ➔ 4.56 * 10^-2 ➔ Magnitude = -2
        # figs - magnitude - 1 -> Calculates exact decimal position to round to.
        # based from -magnitude + (figs-1)
        p = figs - int(math.floor(math.log10(abs(ans)))) - 1

        res = round(ans, p)

        # If p <= 0, we rounded to a whole number (like 460.0).
        # We cast to int() to drop the '.0' so it doesn't look like an extra sig fig.
        print(f"Answer: {int(res) if p <= 0 else res}")
