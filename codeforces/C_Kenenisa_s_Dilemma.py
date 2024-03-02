n = int(input())
nums = list(map(int, input().split()))

swaps = []

for i in range(n - 1):
    if nums[i] > nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
        swaps.append([i, i+1])


print(len(swaps))
for swap in swaps:
    print(*swap)
