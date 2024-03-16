n, m, k = list(map(int, input().split()))

to_olympiad = {}  # dep -> arrival
back_home = {}  # dep -> arrival

for _ in range(m):
    # dep day, dep city, arrival city, cost
    d, f, t, c = list(map(int, input().split()))

    metro = 0  # Since the cities are from 0 -> n where 0 is the metro

    if f > 0:
        journey = (f, metro)  # f -> t(arrival is at metro)
        if journey in to_olympiad:
            to_olympiad[journey] = to_olympiad[journey] if to_olympiad[journey][0] < d else [
                d, c]
        else:
            to_olympiad[journey] = [d, c]
    else:
        journey = (metro, t)  # f(metro) -> t(arrival is at back home)
        if journey in back_home:
            back_home[journey] = back_home[journey] if back_home[journey][0] < d else [
                d, c]
        else:
            back_home[journey] = [d, c]


# If this is more then their not going back at all
to_olympiad_count = len(to_olympiad.keys())
# If this is more then their not going back to their city
back_to_home_count = len(back_home.keys())
if to_olympiad_count > back_to_home_count or to_olympiad_count < back_to_home_count:
    print(-1)
else:
    total = sum([y for x, y in to_olympiad.values()]) + \
        sum([y for x, y in back_home.values()])

    print(total)


""" 
     n cities means n jury members 
     2 6 5
     To olympiad 
        1 1 0 5000
        3 2 0 5500
        2 2 0 6000

        1 -> 0, earliest day is 1
        2 -> 0, earliest day is 2

    Back olympiad 
        15 0 2 9000
        9 0 1 7000
        8 0 2 6500

        0 -> 1, earliest day is 9
        0 -> 2, earliest day is 8

    Total comes out too: 24500


"""
