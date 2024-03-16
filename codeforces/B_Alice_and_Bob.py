t = int(input())

for _ in range(t):
    n, m, k = list(map(int, input().split()))
    a = sorted(input())
    b = sorted(input())

    e = ""
    i, j = 0, 0

    while i < n and j < m:
        limit_a = min(k, n - i)
        limit_b = min(k, m - j)

        for _ in range(limit_a):
            e += a[i]
            i += 1

        for _ in range(limit_b):
            e += b[j]
            j += 1

    while i < n:
        e += a[i]
        i += 1

    while j < m:
        e += b[j]
        j += 1

    print(e)
