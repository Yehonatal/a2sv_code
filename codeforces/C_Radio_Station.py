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
n, m = i_obj.toList()
servers = {}
for _ in range(n):
    names, ip = i_obj.toStrList()
    servers[ip] = names

for _ in range(m):
    names, ip = i_obj.toStrList()
    fixed_ip = ip.replace(";", "")
    print(f"{names} {ip} #{servers[fixed_ip]}")
