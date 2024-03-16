def nextPermutation(nums):
    right, r_right = len(nums) - 2, len(nums) - 1  # right, right most elements

    def next_larger(num, lst):
        larger = [x for x in lst if x > num]
        if larger:
            return min(larger)

    while right >= 0:
        # if r_right is lower then right just swap them
        if nums[right] < nums[r_right]:
            edge = sorted(nums[right:])  # O(n)
            if len(edge) > 2:
                # pick the next larger value then right
                i = edge.index(next_larger(nums[right], edge))
                left = edge.pop(i)
                nums[right:] = [left] + edge
            else:
                nums[r_right], nums[right] = nums[right], nums[r_right]
            return

        r_right = right
        right -= 1

    # finally if nothing works then we'll just sort the list
    nums.sort()  # O(nlogn)


nums = [1, 5, 1]
print(nextPermutation(nums))
print(nums)
# nums = [2, 3, 1]
# print(nextPermutation(nums))
# print(nums)
# nums = [1, 2, 3]
# print(nextPermutation(nums))
# print(nums)
# nums = [3, 2, 1]
# print(nextPermutation(nums))
# print(nums)
# nums = [1, 1, 5]
# print(nextPermutation(nums))
# print(nums)
# nums = [4, 3, 2, 5, 4, 1, 3]
# print(nextPermutation(nums))
# print(nums)
# nums = [4, 3, 2, 5, 4, 3, 1]
# print(nextPermutation(nums))
# print(nums)
# nums = [4, 3, 2, 2, 5, 3, 1]
# print(nextPermutation(nums))
# print(nums)
