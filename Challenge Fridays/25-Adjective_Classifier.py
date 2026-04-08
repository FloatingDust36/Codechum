words = input("Enter adjective: ").split()

is_more = words[0] == "more"
is_most = words[0] == "most"
is_er = words[-1].endswith("er")
is_est = words[-1].endswith("est")

if (is_more or is_most) and (is_er or is_est):
    print("WRONG")
elif is_more or is_er:
    print("COMPARATIVE")
elif is_most or is_est:
    print("SUPERLATIVE")
else:
    print("POSITIVE")
