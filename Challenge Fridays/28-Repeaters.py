from collections import Counter

s = input("Enter string: ").lower()

counts = Counter(s)

repeaters = [(k, v) for k, v in counts.items() if v > 1]

if not repeaters:
    print("No repeaters")
else:
    # Sort with a lambda:
    # -x[1] sorts frequency in descending order (highest first)
    # x[0] acts as the tie-breaker, sorting alphabetically ascending
    for k, v in sorted(repeaters, key=lambda x: (-x[1], x[0])):
        print(f"{k} {v}")
