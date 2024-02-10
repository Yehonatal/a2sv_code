def shortestToChar(s, c):
    chars = [i for i, char in enumerate(s) if char == c]
    # print(chars)

    result = []
    prev_limit = 0
    for limit in chars:
        # print(prev_limit, limit + 1)
        # result.append([x for x in s[prev_limit:limit+1]])
        result += [abs(i - limit)
                   for i in range(prev_limit, prev_limit + len(s[prev_limit:limit+1]))]
        # result.append([abs(i - limit)
        #                for i in range(prev_limit, prev_limit + len(s[prev_limit:limit+1]))])
        prev_limit = limit + 1

    return result


s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
# print("[3,2,1,0,1,0,0,1,2,2,1,0]")
