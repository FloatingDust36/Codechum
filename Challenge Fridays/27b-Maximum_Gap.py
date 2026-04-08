n = int(input("Enter the number of elements: "))

if n < 2:
    print("Maximum difference between two successive elements: 0")
else:
    arr = [int(input(f"Enter element {i+1}: ")) for i in range(n)]

    max_gap = max(abs(a - b) for a, b in zip(arr, arr[1:]))

    print(f"Maximum difference between two successive elements: {max_gap}")
