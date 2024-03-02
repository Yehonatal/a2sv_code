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
        for i in range(n):
            for j in range((n-1) - i):
                if arr1[j] < arr1[j+1] and arr2[j] < arr2[j+1]:
                    arr1[j], arr1[j+1] = arr1[j+1], arr1[j]
                    arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
                    swaps.append([i, j+1])

        print(len(swaps))
        for swap in swaps:
            print(*swap)
