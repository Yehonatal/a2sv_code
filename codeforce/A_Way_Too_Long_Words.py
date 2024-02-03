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

    def toList_(self, sign):
        return list(map(int, input().split(sign)))

    # string - set
    def toSet(self):
        return set([c for c in input()])


i_obj = I()

for _ in range(i_obj.inInt()):
    word = i_obj.inStr()
    if i_obj.strLen(word) > 10:
        print(word[0] + str(i_obj.strLen(word[1:-1])) + word[-1])
    else:
        print(word)
