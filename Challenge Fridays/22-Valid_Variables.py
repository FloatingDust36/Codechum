vars = []
while (s := input("Enter variable: ")) != "STOP":
    vars.append(s)

valid = [v for v in vars if v.isidentifier()]

print("\nValid Variable Names:")
print("\n".join(valid) if valid else "(none)")
