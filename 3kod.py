def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

input_str = input("Enter numbers separated by spaces: ")
input_list = list(map(int, input_str.split()))

bubble_sort(input_list)
print("Sorted numbers are:", input_list)
