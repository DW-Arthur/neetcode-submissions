class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1 , 1, 2, 8
        #  48 24 6 1  
        prefix = [1 for i in range(len(nums))]
        postfix = [1 for i in range(len(nums))]
        result = []
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
            print(prefix)
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i +1] * nums[i+1]
            print(postfix)
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])
        return result

