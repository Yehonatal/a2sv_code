from itertools import combinations

n, target = list(map(int, input().split()))
nums = list(map(int, input().split()))

found = [x for x in combinations([i for i in range(1, n+1)], 4) if sum([
    nums[y-1] for y in x]) == target]

if found:
    print(' '.join(map(str, found[0])))
else:
    print("IMPOSSIBLE")
