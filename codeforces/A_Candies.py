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

for _ in range(i_obj.inInt()):
    n = i_obj.inInt()
    for k in range(2, 36):
        den = 2 ** k - 1

        if n % den:
            continue
        x = n // den
        break
    print(x)
