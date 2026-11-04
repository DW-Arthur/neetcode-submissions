from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Mid is on the left/upper plateau: minimum is to the right
            if nums[mid] > nums[right]:
                left = mid + 1
            # Mid is on the right/lower plateau (or array is fully sorted):
            # minimum is at mid or to the left of mid
            else:
                right = mid

        # Loop ends when left == right, pointing directly at the minimum
        return nums[left]