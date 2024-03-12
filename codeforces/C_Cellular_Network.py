n, m = list(map(int, input().split()))
cities = list(map(int, input().split()))
towers = list(map(int, input().split()))


def find_nearest_tower(city, towers):
    l, r = 0, len(towers) - 1

    while l < r:
        m = (l + r) // 2
        if towers[m] < city:
            l = m + 1
        else:
            r = m

    if l == 0:
        return abs(city - towers[l])
    elif l == len(towers):
        return abs(city - towers[left - 1])
    else:
        return min(abs(city - towers[l]), abs(city - towers[l - 1]))


r = 0
for city in cities:
    min_range_to_tower = find_nearest_tower(city, towers)  # Binary search
    r = max(r, min_range_to_tower)

print(r)
