n, m = list(map(int, input().split()))  # 1 - n and num of problems
problems = list(map(int, input().split()))  # 1 round after else 0

pool = []
other = []

for p in problems:
    if p not in pool:
        pool.append(p)
    else:
        other.append(p)

    if (len(pool) == n and max(pool) == n):
        pool.clear()
        pool.extend(other)
        print("1", end='')
    else:
        print("0", end='')
