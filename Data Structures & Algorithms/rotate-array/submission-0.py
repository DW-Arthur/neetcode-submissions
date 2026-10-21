class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Naive solution? Have a copy of the array
        # use mod function to place the out of bounds array
        length = len(nums)
        copy = nums.copy()
        for i in range(length):
            idx = (i +k) % length
            print(idx)
            nums[idx] = copy[i]

            

        