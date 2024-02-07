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

for _ in range(i_obj.inInt()):
    e = i_obj.inInt()
    nums = i_obj.toList()

    ans = 0
    i = 0
    while i < e:
        j = i
        mx = nums[i]

        while j < e and i_obj.sign(nums[i]) == i_obj.sign(nums[j]):
            mx = max(nums[j], mx)
            j += 1
        i = j
        ans += mx

    print(ans)
