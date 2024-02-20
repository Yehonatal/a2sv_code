from collections import defaultdict

n, q = list(map(int, input().split()))
words = input().split()

pre_suf_i = defaultdict(lambda: -1)

for index, word in enumerate(words):
    pre = ''

    for l in word:
        pre += l

        for i in range(len(word)):
            suf = word[i:]
            pre_suf_i[(pre, suf)] = index


for _ in range(q):
    pre, suf = input().split()

    print(pre_suf_i[(pre, suf)])
