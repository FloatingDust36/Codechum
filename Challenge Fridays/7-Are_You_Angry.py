s = input("Text: ")
count = sum(c.isupper() for c in s)
print("You are angry." if count > 5 else "You're fine, really.")
