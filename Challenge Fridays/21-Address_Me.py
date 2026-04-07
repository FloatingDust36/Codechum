addr = [p.strip() for p in input("Enter address: ").split(",")]

last = addr[-1].split()
zip_code = last.pop() if last[-1].isdigit() else None
addr[-1] = " ".join(last)

for k, v in zip(["Street", "Barangay", "Town", "Province"][4 - len(addr):], addr):
    print(f"{k}: {v}")

if zip_code:
    print(f"Zip Code: {zip_code}")

######

addr = [p.strip() for p in input("Enter address: ").split(",")]

# 1. Handle the Zip Code
last = addr[-1].split()
zip_code = last.pop() if last[-1].isdigit() else None
addr[-1] = " ".join(last)

labels = ["Street", "Barangay", "Town", "Province"]

offset = 4 - len(addr)

for i in range(len(addr)):
    print(f"{labels[i + offset]}: {addr[i]}")

if zip_code:
    print(f"Zip Code: {zip_code}")
