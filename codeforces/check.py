class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pairs_max = 0
        nums.sort()  # O(nlogn)
        left, right = 0, len(nums) - 1

        while left < right:
            pairs_max = max(pairs_max, nums[left] + nums[right])
            left += 1
            right -= 1

        return pairs_max


'''
    # 1 :
        What i did:
            [3,5,4,2,4,6] sort it 
            [2,3,4,5,6,2] pairs are picked using a inward walking pointers from the left and right side 
            which would be mean their are a pair with a min,max value from the list
            and just return the max pair count 

'''
