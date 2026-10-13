class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1

        while i < n:
            if nums[i] == nums[i - 1]:
                # Shift all subsequent elements one step left to overwrite the duplicate
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                # The effective array shrinks by 1
                n -= 1
            else:
                # Only move forward if nums[i] is a distinct new value
                i += 1

        return n