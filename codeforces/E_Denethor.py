t = int(input())

for _ in range(t):
    n = int(input())
    first = list(map(int, input().split()))[::-1]
    last = list(map(int, input().split()))[::-1]
    cowards_lol = 0

    start = 0  # The start get moved towards the end(start)
    for end in range(n):
        while start < n:
            if first[start] == last[end]:
                cowards_lol += 1
                break
            start += 1

    print(n - cowards_lol)
