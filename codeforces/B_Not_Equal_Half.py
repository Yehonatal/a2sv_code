n = int(input())
nums = list(map(int, input().split()))

nums.sort()

left = sum(nums[:n])
right = sum(nums[n:])


if left != right:
    print(*nums)
else:
    print(-1)
