def check(s):
    n = len(s.split())
    table = [" "] * n

    for word in s:
        table[int(word[-1]) - 1] = word[:-1]

    return table


s = "is2 sentence4 This1 a3"
print(check(s))
