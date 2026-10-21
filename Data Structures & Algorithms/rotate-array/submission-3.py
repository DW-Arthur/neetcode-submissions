class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # Reversal method
        def reverse(left, right):
            while left <right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left +=1
                right -=1
            
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
            