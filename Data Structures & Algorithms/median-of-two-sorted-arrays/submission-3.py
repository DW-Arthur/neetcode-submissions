from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first, second = 0, 0
        prev, curr = 0, 0
        total = len(nums1) + len(nums2)

        for i in range(total//2+1):
            prev = curr  # Save the previous middle candidate before overwriting curr
            if first < len(nums1) and (second >= len(nums2) or nums1[first] <=nums2[second]):
                curr = nums1[first]
                first +=1
            else:
                curr = nums2[second]
                second +=1
        # 1 2 3 4 
        if total %2 ==0:
            return (prev + curr) / 2.0
        else:
            return float(curr)