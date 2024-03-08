t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if arr1 == sorted(arr1) and arr2 == sorted(arr2):
        print(0)
    elif len(arr1) < 3:
        print(-1)
    else:
        swaps = []
        swapped = True
        while swapped:
            swapped = False
            for i in range(n - 1):
                if arr1[i] > arr1[i+1] or arr2[i] > arr2[i+1]:
                    arr1[i], arr1[i+1] = arr1[i+1], arr1[i]
                    arr2[i], arr2[i+1] = arr2[i+1], arr2[i]
                    swaps.append([i, i+1])
                    swapped = True

        print(len(swaps))
        for swap in swaps:
            print(*swap)
