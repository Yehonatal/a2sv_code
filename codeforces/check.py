def flipgame(fronts, backs):

    # uni = list(set(fronts + backs))
    # good = []
    # for i in range(len(uni)):
    #     if fronts[i] != backs[i] != uni[i]:
    #         good.append(uni[i])

    # return min(good) if len(good) else 0

    seen = set()
    doubles = set()

    for f, b in zip(fronts, backs):
        seen.add(f)
        seen.add(b)

        if f == b:
            doubles.add(f)

    return min(seen - doubles, default=0)


fronts = [1, 2, 4, 4, 7]
backs = [1, 3, 4, 1, 3]
print(flipgame(fronts, backs))


fronts = [1]
backs = [1]
print(flipgame(fronts, backs))
