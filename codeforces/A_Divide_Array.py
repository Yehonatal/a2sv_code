n = int(input())
nums = list(map(int, input().split()))
nums.sort()

print(1, nums[0])

if nums[-1] == 0:
    print(2, nums[1], nums[2])
    print(n-3, *nums[3:])
else:
    print(1, nums[-1])
    print(n-2, *nums[1:n-1])
