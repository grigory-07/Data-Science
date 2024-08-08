def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

val = input("Enter the elements:")
arr = list(map(int, val.split()))

print("Values entered: ", arr)
bubble_sort(arr)
print("Sorted List: ", arr)
