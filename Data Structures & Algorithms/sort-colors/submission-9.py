class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Divide the array into 3 sections
        # 0s, 1s, 2s
        # left and right pointer, anything before left is 0, anything after right is 2
        # Anything in between left and right is 1
        left, right = 0, len(nums)-1
        i = 0
        while i <= right:
            if nums[i] == 0:
                #swap left and i
                tmp = nums[left]
                nums[left] = 0
                nums[i] = tmp
                left+=1
                i += 1
                continue
            if nums[i] ==1:
                i +=1
                continue
            if nums[i] ==2:
                tmp = nums[right]
                nums[i] = nums[right]
                nums[right] = 2
                right -=1
                continue
        return nums