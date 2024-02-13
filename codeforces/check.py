def largestPerimeter(nums):
    nums.sort()
    res = 0

    for i in range(len(nums)-2):
        if nums[i] + nums[i+1] > nums[i+2]:
            res = max(res, sum(nums[i:i+3]))

    return res


nums = [2, 1, 2]
print(largestPerimeter(nums))
nums = [1, 2, 1, 10]
print(largestPerimeter(nums))
