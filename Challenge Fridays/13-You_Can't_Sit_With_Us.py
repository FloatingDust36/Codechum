n = int(input("Number of strings: "))
strings = [input(f"Enter string {i+1}: ") for i in range(n)]
ch = input("Enter excluded character: ")

res = [s for s in strings if ch not in s][::-1]

if res:
    print("\nYou belong with us:")
    print("\n".join(res))
else:
    print("\nNo one belongs")
