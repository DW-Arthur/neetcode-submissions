class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Somehow find the inflection point, which seperates the rotated part of the array
        # [3, 4, 5, 6, 1, 2]
        #  0, 1, 2, 3, 4, 5
        # left = 3 , right = 2, mid = 2 ( 5)
        # left > mid, right < mid
        # Search the right segment?
        # Move the left to mid +1? left= 2+1 = 3
        # left =6, right = 2, mid = (3+5) /2 = 4 == 1
        # left > mid, right > mid
        # return mid, since mid is now in the inflection point, as both left and right
        # pointer from either side of the rotated array is bigger
        # [4, 5, 0, 1, 2, 3]
        #  0, 1, 2, 3, 4, 5
        # left =4, right = 3, mid = 0
        # left >4, right > 0, return mid
        # [4, 5, 6, 7]
        #  0, 1, 2, 3
        # left = 4, right = 7, mid = 5
        # left < mid,right > mid, right = mid -1, 0
        # left <= right , breaks loop
        # return left
        left, right = 0, len(nums) -1
        while left <=right:
            mid = (left +right)//2
            if nums[left] > nums[mid] and nums[right]> nums[mid]:
                return nums[mid]
            if nums[left] < nums[mid]:
                left = mid+1
            elif nums[right] > nums[mid]:
                right = mid -1
        return nums[left]