def strStr(haystack, needle):
    n = len(needle) - 1
    i = j = 0

    while i <= len(haystack) and (len(haystack) - i) > n:
        if j == n:
            return i - n
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            i += 1
            j = 0

    return -1


haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))
haystack = "leetcode"
needle = "leet"
print(strStr(haystack, needle))
haystack = "leetcode"
needle = "code"
print(strStr(haystack, needle))
