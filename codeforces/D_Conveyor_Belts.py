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

t = i_obj.inInt()
for _ in range(t):
    n, x1, y1, x2, y2 = i_obj.toList()

    # layer for the first point
    a = min(x1, y1)
    b = min(n-x1 + 1, n-y1 + 1)
    later1 = min(a, b)

    # layer for the second point
    c = min(x2, y2)
    d = min(n - x2 + 1, n - y2 + 1)
    layer2 = min(c, d)
    #  diff layer1 and layer 2

    print(abs(later1 - layer2))
