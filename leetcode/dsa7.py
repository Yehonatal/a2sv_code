def findMaxConsecutiveOnes(nums):
    count = 0

    i, j = 0, 0
    while j < len(nums):
        if nums[j] == 0:
            count = max(count, j - i)
            i = j + 1
        j += 1

    count = max(count, j - i)
    return count


print(findMaxConsecutiveOnes([1]))
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
print(findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
""" 
    - [1, 1, 0, 1, 1, 1]
             |
                      |
       0             3
"""
