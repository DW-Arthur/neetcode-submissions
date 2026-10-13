class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Quick Sort Partitioning method, 1 Pass
        # Essenitally 3 sections, the 0s, 1s ,and 2s,
        # 2 pointers, left is always pointing at 1, anything to the left of 1 is 
        # going to be 0, anything to the right of the right pointer is 2, 
        # Everything in between and at the poitner of left/right is gonna be 1
        # Algorithm
        # Have a left pointer and right pointer, and an i pointer
        # If i encounters 0, swap the i with left immediately
        # Move the left pointer up to the i, since that has been swapped, and all
        # the left part of the array is 0, 
        # When i reaches 2, swap i and right pointer, move the right pointer inwards
        # DO not increment i, as the swapped i maybe 0, incremeent it would trap a 0
        # in between 1 and 2
        # Keep going until i reach past Right pointer
        # I don't think I need to swap i and left, but i do need to move the left poitner 
        # if i is 1
        left,right = 0, len(nums)-1
        i = 0
        # Should it be i <right or i <=right
        def swap(i,j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp

        while i <= right and left <right :
            if nums[i] == 1:
                i+=1
                continue
            if nums[i] == 0:
                swap(i, left)
                left +=1
                i+=1
                continue
            if nums[i] == 2:
                swap(i,right)
                right -=1
                continue
        return nums


        