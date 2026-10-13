class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup = dict()
        for i in range(len(nums)):
            if target - nums[i] in dup:
                return [dup[target - nums[i]], i]
            dup[nums[i]] = i