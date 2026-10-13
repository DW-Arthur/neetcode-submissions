class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        seen = {}
        for i in range(len(nums)):
            if target-nums[i] in seen:
                result = [seen[target-nums[i]], i]
                return result
            seen[nums[i]] = i
        