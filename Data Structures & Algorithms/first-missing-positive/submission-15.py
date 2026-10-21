class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # First purge all the negative numbers and numbers more than the length of the array
        n = len(nums)
        for i in range(len(nums)):
            if nums[i] > n or nums[i] <=0:
                nums[i] = n+1
        # Begin negative marking on the available array
        for i in range(len(nums)):
            # I need abs value, incase I already negatively marked it
            current = abs(nums[i])
            if current <=n:
                nums[current-1] = -abs(nums[current-1])

        # Go through the array again, the first index non negative is the first missing 
        # positive
        for i in range(len(nums)):
            if nums[i] >0:
                return i +1
        return n+1
        