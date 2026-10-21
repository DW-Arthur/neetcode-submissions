class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result =1
        nums.sort()
        for i in nums:
            if i == result:
                result  +=1
            elif i > result:
                break
        return result