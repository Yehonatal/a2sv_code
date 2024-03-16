t = int(input())

for _ in range(t):
    c = "codeforces"
    s = input()

    counter = 0
    i, j = 0, 0

    while j < len(c):
        if s[i] != c[j]:
            counter += 1
        i += 1
        j += 1

    print(counter)
