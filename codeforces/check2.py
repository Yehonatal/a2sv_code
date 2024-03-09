def fourSum(nums, target):
    # A + B + C + D  = target
    quadruplets = []

    def nSum(left, right, target, n, path, quadruplets):
        # n(4) numbers that add up to target
        if right - left + 1 < n or n < 2 or target < nums[left] * n or target > nums[right] * n:
            return

        if n == 2:  # TwoSum
            while left < right:
                sm = nums[left] + nums[right]
                if sm == target:
                    quadruplets.append(path + [nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sm < target:
                    left += 1
                else:
                    right -= 1
            return

        # For n above 2
        for i in range(left, right + 1):
            if i > left and nums[i] == nums[i - 1]:
                continue
            # Next Sum for the inner sum
            # function takes: new_start, length, new_target(target minus chosen elem) , n, path, answerList
            nSum(i+1, right, target - nums[i],
                 n - 1, path + [nums[i]], quadruplets)

    nums.sort()  # O(nlogn)
    # function takes: start, length, target, n, path, answerList
    nSum(0, len(nums) - 1, target, 4, [], quadruplets)
    return quadruplets


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
nums = [2, 2, 2, 2, 2]
target = 8
print(fourSum(nums, target))
