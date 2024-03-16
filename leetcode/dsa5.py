def pancakeSort(arr):
    flips = []
    for i in range(len(arr), 1, -1):  # O(n)
        k = arr.index(i)
        flips += [k + 1, i]
        arr = arr[:k:-1] + arr[:k]  # O(n)

    return flips


print(pancakeSort([3, 2, 4, 1]))
