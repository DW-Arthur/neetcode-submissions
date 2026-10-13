class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        
        maxNum = 1
        current = 1
        
        for i in range(1, len(nums)):
            # Duplicate: skip it, don't break the streak or increment
            if nums[i] == nums[i - 1]:
                continue
            
            # Consecutive element: extend the streak
            if nums[i] - nums[i - 1] == 1:
                current += 1
                maxNum = max(current, maxNum)
            # Streak broken: reset
            else:
                current = 1
                
        return maxNum