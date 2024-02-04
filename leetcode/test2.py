def bs(nums, x):
    if len(nums) == 0:
        return False

    l = 0
    h = len(nums) - 1

    while l <= h:
        mid = l + (h - l) // 2

        if nums[mid] == x:
            return True

        if nums[mid] > x:
            h = mid - 1
        elif nums[mid] < x:
            l = mid + 1

    return False


nums = [10, 11, 16, 20, 23, 30, 34, 60]
print(bs(nums, 11))
