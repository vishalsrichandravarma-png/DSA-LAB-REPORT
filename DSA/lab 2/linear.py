def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1
arr = []
arr = list(map(int, input("Enter elements of the array separated by space: ").split()))
key = int(input("Enter the element to search for: "))
result = linear_search(arr, key)
if result != -1:
    print(f"Element found at index: {result}")  
else:
    print("Element not found in the array.")