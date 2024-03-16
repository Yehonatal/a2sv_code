def removeDuplicates(nums):
    i, j = 0, 1

    while j <= len(nums):

        while j < len(nums) and nums[i] == nums[j]:
            j += 1

        print(nums[i:j])
        if not j - i <= 2:
            del nums[i+2:j]

        # move the pointers
        i = j - 1
        j += 1

    return len(nums), nums


nums = [0, 0, 1, 1, 1, 1, 2, 2, 2, 4]
print(removeDuplicates(nums))
