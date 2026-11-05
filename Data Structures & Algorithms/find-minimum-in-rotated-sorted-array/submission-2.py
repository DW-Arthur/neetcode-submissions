class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        # 4, 5, 6, 1, 2
        # 0, 1, 2, 3, 4
        # left =4, right =2, mid = 6
        # This means the mid is in the upper (rotated part of the range)
        # The mid should go to the right side more, since the minimum is to the right
        # In this case, ignore all elements to the left, left = mid +1
        # 1, 2, 3, 4, 5
        # 0, 1, 2, 3, 4
        # left =1 ,right = 5, mid = 3
        # mid < right, this means everything to the right is higher (could there be an exception?), 
        # If everything above is higher, remove the upper limit, only look at the left
        # Move the right pointer to mid, since mid could be it 
        # 4, 5, 1, 2, 3
        # 0, 1, 2 ,3, 4
        # left=4 , right = 3, mid = 1
        # 4, 5, 1
        # left =4, right =1 , mid = 5
        # mid > right, the minimum is now to the right, delete all the left elements
        # left = mid +1, left = 1, right = 1
        # loop ends when left == right,
        while left < right:
            mid = (left + right) //2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid
        return nums[left]