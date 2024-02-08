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
val = 0
for _ in range(i_obj.inInt()):
    op = i_obj.inStr()
    if op.startswith("+") or op.endswith("+"):
        val += 1
    elif op.startswith("-") or op.endswith("-"):
        val -= 1
print(val)
