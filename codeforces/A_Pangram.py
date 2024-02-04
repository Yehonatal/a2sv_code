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
alphabet = [0] * 26
count = i_obj.inInt()
word = i_obj.inStr()

for c in word.lower():
    alphabet[ord(c) - ord("a")] = 1

if not alphabet.count(0):
    print("YES")
else:
    print("NO")
