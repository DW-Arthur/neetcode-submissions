class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Add nums2 from the end
        # Techinically 3 pointers to this problem
        current = len(nums1) -1
        first,second = m-1,n-1
        while second >=0:
            if first >= 0 and nums1[first] >= nums2[second]:
                nums1[current] = nums1[first]
                current -=1
                first -=1
            elif first < 0 or nums1[first] <nums2[second]:
                nums1[current] = nums2[second]
                current -=1
                second -=1
        