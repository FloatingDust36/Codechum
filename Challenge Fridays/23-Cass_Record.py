def print_sorted_records(records):
    # Sort by score descending (-x[2]), then last name ascending (x[0]), then first name (x[1])
    sorted_records = sorted(records, key=lambda x: (-x[2], x[0], x[1]))

    print("\nSorted List:")
    for last, first, score in sorted_records:
        print(f"{last}, {first} - {score}")


temp_list = []
while True:
    last = input("Enter last name: ")
    if last == "STOP":
        break
    first = input("Enter first name: ")
    score = int(input("Enter score: "))
    print()  # To match the empty line spacing in the sample output

    temp_list.append((last, first, score))

# Convert to a tuple of tuples to strictly satisfy the problem's constraints
records_tuple = tuple(temp_list)
print_sorted_records(records_tuple)

###########


def print_sorted_records(records):
    # .sort() modifies the list in-place. Faster and takes less memory!
    records.sort(key=lambda x: (-x[2], x[0], x[1]))

    print("\nSorted List:")
    for last, first, score in records:
        print(f"{last}, {first} - {score}")


records = []
while True:
    last = input("Enter last name: ")
    if last == "STOP":
        break
    first = input("Enter first name: ")
    score = int(input("Enter score: "))
    print()

    # We append a tuple of the student data into our list
    records.append([last, first, score])

# Pass the list directly. No unnecessary casting!
print_sorted_records(records)
