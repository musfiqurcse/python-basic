class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # find the single number which is not repeated twice
        # Input: [2,2,1,1,5,5,6,6,7]
        # Output: 7
        return sum(list(set(nums))) *2 - sum(nums)
            
