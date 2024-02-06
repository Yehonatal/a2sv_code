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
    if n < 4 or (n // 2) % 2 != 0:
        print('NO')
    else:
        print("YES")
        even = [2, 4]
        odd = [1, 5]

        for i in range(2, n//2):
            # even at 2 = even at 0 (2) + 6, even at 3 = even at 1 (4) + 6
            even.append(even[i-2] + 6)
            # odd at 2 = odd at 0 (1) + 6, odd at 3 = odd at 1 (5) + 6
            odd.append(odd[i-2] + 6)
        output = even + odd
        for num in output:
            print(num, end=" ")
        print()
