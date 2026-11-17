from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        left = 0

        for right in range(k - 1, len(nums)):
            current = float('-inf')
            for i in range(left, right + 1):
                current = max(current, nums[i])
            result.append(current)
            left += 1

        return result