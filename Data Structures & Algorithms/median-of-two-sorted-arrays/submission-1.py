from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first, second = 0, 0
        count = 0
        prev, curr = 0, 0
        total = len(nums1) + len(nums2)

        while count < total // 2 + 1:
            prev = curr  # Save the previous middle candidate before overwriting curr

            # Must guard against first or second going out of bounds!
            if first < len(nums1) and (second >= len(nums2) or nums1[first] <= nums2[second]):
                curr = nums1[first]  # Grab the value BEFORE moving first past it
                first += 1
            else:
                curr = nums2[second] # Grab the value BEFORE moving second past it
                second += 1

            count += 1

        if total % 2 == 0:
            return (prev + curr) / 2.0
        else:
            return float(curr)