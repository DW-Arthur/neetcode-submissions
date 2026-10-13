class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Insert the elements at the end, since nums2 is guaranteed to go to nums1
        first = m - 1
        second = n - 1
        current = len(nums1)-1

        while second >= 0:
            if first >= 0 and nums1[first] > nums2[second]:
                nums1[current] = nums1[first]
                first -= 1
            else:
                nums1[current] = nums2[second]
                second -= 1
            current -= 1