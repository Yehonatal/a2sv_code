from collections import Counter
n = int(input())


res = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

# ai = bj * cj
a_counts = Counter(a)

res = 0

for x in b:
    for y in c:
        if x * y in a_counts:
            res += a_counts[x * y]

print(res)
