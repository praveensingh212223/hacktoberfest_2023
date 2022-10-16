# Initialize array
arr1 = [1, 2, 3, 4, 5]

# Create another array arr2 with size of arr1
arr2 = [None] * len(arr1)

# Copying all elements of one array into another
for i in range(0, len(arr1)):
    arr2[i] = arr1[i]

# Displaying elements of array arr1
print("Elements of original array: ")
for i in range(0, len(arr1)):
    print(arr1[i]),

print()

# Displaying elements of array arr2
print("Elements of new array: ")
for i in range(0, len(arr2)):
    print(arr2[i]),
