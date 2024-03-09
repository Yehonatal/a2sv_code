n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    for j in range(0, n-i-1):
        is_odd = (nums[j] + nums[j+1]) % 2 != 0
        if is_odd and nums[j+1] < nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(*nums)

""" 
# 1 : Working solution 
    
odd = [num for num in nums if num % 2 != 0]
even = [num for num in nums if num % 2 == 0]

if len(odd) and len(even):
    nums.sort()
    print(*nums)
else:
    print(*nums)
 """

# i, j = 0, 1
# while j < n:
#     is_odd = True if (nums[i] + nums[j]) % 2 != 0 else False
#     # if odd and if j is lower number then i swap to get the smallest lex order
#     if is_odd and nums[j] < nums[i]:
#         nums[j], nums[i] = nums[i], nums[j]

#     i += 1
#     j += 1
