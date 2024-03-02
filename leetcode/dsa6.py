def reductionOperations(nums):
    count = nxt_lg = 0
    volt = {}
    for num in nums:  # I can use Counter from collections
        volt[num] = volt.get(num, 0) + 1

    for k in sorted(volt, reverse=True):
        if len(volt) > 1:
            # until there is only 1 distinct element in the volt
            nxt_lg += volt.pop(k)
            count += nxt_lg

    return count


def easy(nums):
    nums.sort(reverse=True)  # O(nlogn)
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            count += i + 1

    return count


nums = [5, 1, 3]  # 5 3 1 , count = 0 + 1, 1 + 1
# print(easy(nums))
print(reductionOperations(nums))
nums = [1, 1, 1]  # 1 1 1, count 0
# print(easy(nums))
# print(reductionOperations(nums))
nums = [1, 1, 2, 2, 3]  # 3 2 2 1 1, count = 0 + 1, 1 + 2 + 1
# print(easy(nums))
# print(reductionOperations(nums))
