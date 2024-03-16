from collections import Counter


def dividePlayers(skill):
    desired_sum = 2 * sum(skill) // len(skill)

    chemistry = 0
    cnt = Counter(skill)

    for val, count in cnt.items():
        diff = desired_sum - val

        if count != cnt[diff]:
            return -1

        chemistry += count * val * diff

    return chemistry // 2


# skill = [1, 1, 2, 3]
# skill = [3, 4]
skill = [3, 2, 5, 1, 3, 4]
print(dividePlayers(skill))
