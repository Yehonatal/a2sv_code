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
boxes = i_obj.toList()
boxes.sort()
i, j = 0, 1

while j < n:
    if boxes[i] < boxes[j]:
        boxes[i] = "Inside"
    i = j
    j += 1

print(len([x for x in boxes if x != 'Inside']))
