def fourSum(nums, target):
    # A + B + C + D  = target
    if len(nums) < 4:
        return []

    nums.sort()  # O(nlogn)
    quadruplets = []

    # A
    for a in range(len(nums) - 3):
        if a > 0 and nums[a] == nums[a-1]:
            continue

        # B
        for b in range(a + 1, len(nums) - 2):
            if b > a + 1 and nums[b] == nums[b-1]:
                continue

            c = b + 1
            d = len(nums) - 1

            # C & D
            while c < d:
                quad_sum = nums[a] + nums[b] + nums[c] + nums[d]

                if quad_sum == target:
                    quadruplets.append([nums[a], nums[b], nums[c], nums[d]])
                    c += 1
                    d -= 1

                    while c < d and nums[c] == nums[c-1]:
                        c += 1
                    while c < d and nums[d] == nums[d+1]:
                        d -= 1
                elif quad_sum < target:
                    c += 1
                else:
                    d -= 1

    return quadruplets


nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))
nums = [2, 2, 2, 2, 2]
target = 8
print(fourSum(nums, target))
