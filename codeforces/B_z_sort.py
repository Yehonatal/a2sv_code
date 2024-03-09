n = int(input())
nums = list(map(int, input().split()))
nums.sort()
z_sorted = []
l, r = 0, len(nums) - 1

while l < r:
    z_sorted.append(nums[l])
    z_sorted.append(nums[r])
    l, r = l+1, r-1

if l == r:
    z_sorted.append(nums[l])

print(*z_sorted)
