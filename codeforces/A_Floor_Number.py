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
for _ in range(n):
    n, x = i_obj.toList()
    c = 2
    floor_level = 1

    while c < n:
        c += x  # add the number of room to the count of room in the building
        floor_level += 1  # each time you add a floor increment the floor your on

    print(floor_level)
