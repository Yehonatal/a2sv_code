def isLongPressedName(name, typed):
    i, j = 0, 0

    track = True
    while i < len(name):
        while j < len(typed) and typed[j] == name[i]:
            track = False
            j += 1
        else:
            if track:
                return False
            track = True
            i += 1

    return True


# name = "alex"
# typed = "aaleex"
# print(isLongPressedName(name, typed))

# name = "saeed"
# typed = "ssaaedd"
# print(isLongPressedName(name, typed))

name = "leelee"
typed = "lleeelee"
print(isLongPressedName(name, typed))
# https://leetcode.com/problems/long-pressed-name/solutions/1343001/python3-2-pointers/
