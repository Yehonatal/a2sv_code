from collections import Counter


def check(s):
    unique = [x for (x, y) in Counter(s).items() if y == 1]
    return unique[0] if unique else -1


print(check("leetcode"))
print(check("lleettccooddee"))
