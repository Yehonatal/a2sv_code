def merge(word1, word2):
    i, j = 0, 0
    merged_ = []

    while i < len(word1) and j < len(word2):
        merged_.append(word1[i])
        merged_.append(word2[j])
        i, j = i + 1, j + 1

    if i < len(word1):
        merged_.extend(word1[i:])
    if j < len(word2):
        merged_.extend(word2[i:])

    return "".join(merged_)


word1 = "abc"
word2 = "pqr"
print(merge(word1, word2))
