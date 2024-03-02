t = int(input())

for _ in range(t):
    n = int(input())

    m = 0
    lan = {}
    for _ in range(n):
        a, b = list(map(int, input().split()))
        if a in lan:
            lan[a] = max(lan[a], a * b)
        else:
            lan[a] = b

    print(sum(lan.values()))
