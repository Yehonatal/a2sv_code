n = int(input())

for _ in range(n):
    s = list(input())
    count = 0
    l, r = 0, len(s) - 1

    if s[::-1] == s:
        print(count)
        continue

    while l < r:
        if s[r] != s[l]:
            s[r] = s[l]
            l += 1
            r -= 1
            count += 1
        else:
            l += 1
            r -= 1

    print(count)
