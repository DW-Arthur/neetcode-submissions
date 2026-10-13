class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Quick sort partioning 
        # Everything before left pointer is 0, everything between left and right pointer is
        # 1, everything after 1 is 2
        left = 0
        right = len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i] = nums[left]
                nums[left] = 0
                i+=1
                left+=1
                continue
            if nums[i] == 1:
                i+=1
                continue
            if nums[i] ==2:
                nums[i] = nums[right]
                nums[right] =2
                right -=1
        return nums