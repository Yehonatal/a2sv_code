n, q = list(map(int, input().split()))


mapper = {}

words = input().split()
for i, word in enumerate(words):
    mapper[word] = i

# words = input().split()
# mapper = list(enumerate(words))


for _ in range(q):
    pr, sf = input().split()

    # valid = [(index, word)
    #          for index, word in mapper if word.startswith(pr) and word.endswith(sf)]

    # if valid:
    #     print(max(valid)[0])
    # else:
    #     print(-1)

    largest = 0
    is_found = False

    for word, i in mapper.items():
        if word.startswith(pr) and word.endswith(sf):
            is_found = True
            largest = max(largest, i)

    if is_found:
        print(largest)
    else:
        print(-1)
