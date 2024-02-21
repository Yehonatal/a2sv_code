def applyOps(nums):

    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0

    zeros = nums.count(0)  # count the zeros
    nums = [x for x in nums if x != 0]  # new list of ele that are not 0
    nums.extend([0]*zeros)  # extend the list with the zeros attached

    return nums


""" 
    # 1:
        Time: O(n)
        Space: O(n + m)

"""


nums = [1, 2, 2, 1, 1, 0]
print(applyOps(nums))

nums = [0, 1]
print(applyOps(nums))
