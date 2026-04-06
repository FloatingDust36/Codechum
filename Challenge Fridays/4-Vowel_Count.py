sen = input("Enter a sentence: ")

vowels = 'aeiou'
count = 0

for c in sen:
    if c.lower() in vowels:
        count += 1

print(f"Vowels: {count}")
