t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()

    diff = abs(s[0] - s[1])  # we are guaranteed to have at least 2 athletes

    for i in range(len(s) - 1):
        diff = min(diff, abs(s[i] - s[i+1]))

    print(diff)
