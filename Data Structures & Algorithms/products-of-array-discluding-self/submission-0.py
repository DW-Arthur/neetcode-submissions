class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        numZero = 0
        result = [0 for _ in range(len(nums))]
        print(result)
        for i in nums:
            if i == 0:
                numZero +=1
            if i !=0:
                prod = prod * i
        
        if numZero > 1:
            return result
        if numZero == 1:
            for i in range(len(nums)):
                if nums[i] ==0:
                    result[i] = prod
            return result
        for i in range(len(nums)):
            result[i] = prod//nums[i]
        return result