from collections import Counter
n = int(input())


res = 0

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a_counts = Counter(a)

res = 0

for i in c:
    res += a_counts.get(b[i-1], 0)


print(res)
