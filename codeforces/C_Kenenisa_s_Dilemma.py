n = int(input())
nums = list(map(int, input().split()))
count = 0
swaps = []

for i in range(n):
    minn = nums[i]
    min_index = i
    for j in range(i, n):
        if nums[j] < minn:
            minn = nums[j]
            min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]
            count += 1
            swaps.append((i, min_index))

print(count)
for swap in swaps:
    print(*swap)
