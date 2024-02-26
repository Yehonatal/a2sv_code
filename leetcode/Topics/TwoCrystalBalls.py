import random
import math


def two_crystal_balls(breaks):
    jmpAmount = math.floor(math.sqrt(len(breaks)))

    i = jmpAmount
    while i < len(breaks):
        if breaks[i]:  # we found the True value where the ball breaks
            break
        i += jmpAmount

    i -= jmpAmount

    for j in range(jmpAmount):
        if i < len(breaks) and breaks[i]:
            return i
        i += 1
    return -1


idx = random.randint(0, 9999)
data = [False] * 10000

for i in range(idx, 10000):
    data[i] = True

print(two_crystal_balls(data) == idx)
print((two_crystal_balls([False] * 821) == -1))
