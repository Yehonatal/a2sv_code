def countDistinctIntegers(nums):
    res = set()

    for num in nums:
        if num > 9:
            res.add(int(str(num)[::-1]))

        res.add(num)

    return len(res)


nums = [1, 13, 10, 12, 31]
print(countDistinctIntegers(nums))
nums = [2, 2, 2]
print(countDistinctIntegers(nums))
