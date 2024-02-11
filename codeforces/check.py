import string


def replaceDigits(s):
    alphabet = list(string.ascii_lowercase)
    alphabet_lower = {}

    for i, char in enumerate(alphabet):
        alphabet_lower[char] = i

    result = ""
    for i in range(len(s)):
        if s[i].isdigit():
            at = int(alphabet_lower[s[i-1]]) + int(s[i])
            result += alphabet[at]
        else:
            result += s[i]

    return result


s = "a1c1e1"
print(replaceDigits(s))
s = "a1b2c3d4e"
print(replaceDigits(s))
