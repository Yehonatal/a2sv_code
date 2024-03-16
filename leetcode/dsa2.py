def checkPalindromeFormation(a, b):
    def check(a, b, n):
        prefix, suffix = 0, n - 1
        while (prefix < suffix):
            if (a[prefix] != b[suffix]):
                break
            prefix += 1
            suffix -= 1

        xa = a[prefix:suffix + 1]
        xb = b[prefix:suffix + 1]

        if (xa == xa[::-1] or xb == xb[::-1]):
            return True
    return check(a, b, len(a)) or check(b, a, len(a))


# a = "x"
# b = "y"
# print(checkPalindromeFormation(a, b))
# a = "xbdef"
# b = "xecab"
# print(checkPalindromeFormation(a, b))
a = "ulacfd"
b = "jizalu"
print(checkPalindromeFormation(a, b))
# a = "abcedf"
# b = "edfcba"
# print(checkPalindromeFormation(a, b))
# a = "abda"
# b = "acmc"
# print(checkPalindromeFormation(a, b))
