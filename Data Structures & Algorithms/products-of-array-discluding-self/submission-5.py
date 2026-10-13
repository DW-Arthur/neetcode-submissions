class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1 , 1, 2, 8
        #  48 24 6 1  
        result = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(1, len(nums)):
            prefix = prefix * nums[i-1]
            result[i] = result[i] * prefix
        postfix = 1
        for i in range(len(nums)-2, -1, -1):
            postfix = postfix * nums[i+1]
            result[i] = result[i] * postfix
          
        return result

