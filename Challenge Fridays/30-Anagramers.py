s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")

if sorted(filter(str.isalpha, s1.lower())) == sorted(filter(str.isalpha, s2.lower())):
    print(f'"{s1}" and "{s2}" are anagrams.')
else:
    print(f'"{s1}" and "{s2}" are not anagrams.')
