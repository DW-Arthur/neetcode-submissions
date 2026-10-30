class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] > target:
                right = mid - 1        # jump past mid
            elif nums[mid] < target:
                left = mid + 1         # jump past mid
            elif nums[mid] == target:
                return mid

        # When the loop terminates, left is the exact insertion position
        return left