def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    pre = 1
    for i in range(1, n):
        result[i] = pre
        pre *= nums[i]

    post = 1
    for i in range(n - 1, -1, -1):
        result[i] *= post
        post *= nums[i]

    return result


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))

# nums = [-1, 1, 0, -3, 3]
# print(productExceptSelf(nums))
