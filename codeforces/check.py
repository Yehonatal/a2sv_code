def threeSum(nums):
    if len(nums) < 3:
        return []

    nums.sort()  # O(nlogn)
    triplets = []
    # choosing = X
    for x in range(len(nums) - 2):
        # Jump over cases where we have used an elem for x already
        if x > 0 and nums[x] == nums[x-1]:
            continue

        y = x + 1
        z = len(nums) - 1

        # choosing = Y & Z, This is just a normal twoSum solution with pointers
        while y < z:
            sm = nums[x] + nums[y] + nums[z]
            if sm == 0:
                triplets.append([nums[x], nums[y], nums[z]])
                y += 1
                z -= 1

                # Jump over elem if we have used it as y before
                while nums[y] == nums[y-1] and y < z:
                    y += 1
                # Jump over elem if we used it as z before
                while nums[z] == nums[z+1] and y < z:
                    z -= 1
            elif sm < 0:
                y += 1
            else:
                z -= 1

    return triplets


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
nums = [0, 1, 1]
print(threeSum(nums))
nums = [1, 2, -2, -1]
print(threeSum(nums))
