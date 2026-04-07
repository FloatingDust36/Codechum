name = input("Enter name: ")
while (n := int(input("Enter box size: "))) < len(name) + 2:
    print("Choose a larger box.")

h = (n + 1) // 2
for i in range(h):
    print("*" * n if i in (0, h - 1) else "*" +
          (name.center(n - 2) if i == h // 2 else " " * (n - 2)) + "*")
