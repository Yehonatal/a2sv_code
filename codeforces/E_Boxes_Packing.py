from collections import Counter

_ = int(input())
count = Counter(input().split())

print(max(count.values()))
