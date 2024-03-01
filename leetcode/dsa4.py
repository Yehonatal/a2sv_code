def countingSort(arr):
    swaps = 0
    n = len(a)
    swapped = True

    while swapped:
        swapped = False
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps += 1
                swapped = True

    print(f"Array was sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    print(a)


a = [3, 2, 1]
print(countSwaps(arr))
