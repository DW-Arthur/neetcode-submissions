from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            # If the current segment has no rotation, nums[left] is the minimum
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2

            # mid is on the high hill; minimum must be strictly to the right
            if nums[mid] >= nums[left]:
                left = mid + 1
            # mid is on the low hill; it could be the minimum, so keep it
            else:
                right = mid

        return nums[left]