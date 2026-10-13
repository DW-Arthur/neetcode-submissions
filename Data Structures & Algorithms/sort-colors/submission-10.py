class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #3 sections of the array, 0s,1s, and 2s
        # Anything before left pointer is 0, anything after right pointer is 2
        # Anything in between left and right pointer are 1s
        left, right = 0, len(nums)-1
        i=0
        while i <=right:
            if nums[i] ==0:
                #swap left and i
                nums[i] = nums[left]
                nums[left] = 0
                left +=1
                i+=1
            elif nums[i] ==2:
                #swap right and i 
                nums[i] = nums[right]
                nums[right] = 2
                right -=1
                #don't increase i, we don't know what nums[right] is
            elif nums[i] ==1:
                i+=1

        