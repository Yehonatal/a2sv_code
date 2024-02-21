def ribbon_num(n, x, y):
    return min([x, y, n + 1 - x, n + 1 - y])


def min_energy():
    n, x1, y1, x2, y2 = map(int, input().split())

    print(abs(ribbon_num(n, x1, y1) - ribbon_num(n, x2, y2)))


t = int(input())
for _ in range(t):
    min_energy()
