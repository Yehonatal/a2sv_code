class I:
    # String
    def inStr(self):
        return input()

    def strLen(self, word):
        return len(word)

    def inInt(self):
        return int(input())

    # List
    def toList(self):
        return list(map(int, input().split()))

    def toStrList(self):
        return list(map(str, input().split()))

    def toList_(self, sign):
        return list(map(int, input().split(sign)))

    # string - set
    def toSet(self):
        return set([c for c in input()])


i_obj = I()
n = i_obj.inInt()

lvl = 0
cubes = 1
counter = 1

while cubes <= n:
    cubes = ((counter * counter) + counter) / 2

    if cubes > n:
        break

    n = n - cubes
    counter += 1
    lvl += 1

print(lvl)
