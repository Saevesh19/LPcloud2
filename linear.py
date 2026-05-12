def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Taking input from user
n = int(input("Enter number of elements: "))

arr = []

print("Enter elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

target = int(input("Enter element to search: "))

# Function call
result = linear_search(arr, target)

# Display result
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")
