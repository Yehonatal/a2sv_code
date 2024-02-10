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
s = i_obj.inStr()
a = [x for x in s if x == "A"]
d = [x for x in s if x == "D"]


if len(a) > len(d):
    print("Anton")
elif len(a) < len(d):
    print("Danik")
else:
    print("Friendship")
