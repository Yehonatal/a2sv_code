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

    def sign(self, num):
        return num > 0


i_obj = I()
to_center = 0
for i in range(1, 6):
    points = i_obj.toList()
    for j in range(1, 6):
        if points[j-1] == 1:
            to_center = abs(3 - j) + abs(3 - i)

print(to_center)
