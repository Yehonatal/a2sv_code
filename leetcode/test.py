def lengthOfLongestSubstring(s):
    count = 0
    seen = set()
    start, end = 0, 0

    while end < len(s):
        while s[end] in seen:
            seen.remove(s[start])
            start += 1

        seen.add(s[end])
        end += 1
        count = max(count, end - start)

    return count


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
