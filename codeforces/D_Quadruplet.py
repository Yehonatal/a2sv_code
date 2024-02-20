n, target = list(map(int, input().split()))
arr = list(map(int, input().split()))

store = {}

for i, num in enumerate(arr):
    for j in range(i + 1, len(arr)):
        total = arr[i] + arr[j]

        comp = target - total
        if comp in store:
            print(*store[comp], i + 1, j + 1)
            exit()

    for j in range(i):
        total = arr[i] + arr[j]
        store[total] = (j + 1, i + 1)

print("IMPOSSIBLE")
