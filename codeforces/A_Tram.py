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
n = i_obj.inInt()

m = 0
t = 0
for _ in range(n):
    a, b = i_obj.toList()  # out, in
    t += b
    t -= a
    m = max(m, t)
    # m = max(m, m + b - a)
    # m = max(m, (m + b) - a)

print(m)
