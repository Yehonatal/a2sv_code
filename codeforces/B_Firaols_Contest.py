n, m = list(map(int, input().split()))  # 1 - n and num of problems
problems = list(map(int, input().split()))  # 1 round after else 0

pool = {}

for p in problems:
    if p in pool:
        pool[p] += 1
    else:
        pool[p] = 1

    if len(pool) == n:
        print(1, end="")
        for level in range(1, n+1):
            pool[level] = max(0, pool[level] - 1)
            if not pool[level]:
                pool.pop(level)
    else:
        print(0, end="")
