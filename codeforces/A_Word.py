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
word = i_obj.inStr()
upper = len([x for x in word if x.isupper()])
lower = len([x for x in word if x.islower()])
if upper > lower:
    print(word.upper())
else:
    print(word.lower())
