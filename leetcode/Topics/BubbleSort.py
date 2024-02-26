def bubble_sort(arr):

    n = len(arr)

    for i in range(n):
        for j in range((n-1) - i):  # Goes up to the last element that has bubbled up - 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [9, 3, 7, 4, 69, 420, 42]
bubble_sort(arr)

print(arr == [3, 4, 7, 9, 42, 69, 420])
