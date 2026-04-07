name = input("Name: ").lower().split()
uni = input("University: ").replace(" ", "").replace("-", "").lower()

first = "".join(name[:-2]) if "." in name[-2] else "".join(name[:-1])
print(f"Email = {first}.{name[-1]}@{uni}.edu.ph")
