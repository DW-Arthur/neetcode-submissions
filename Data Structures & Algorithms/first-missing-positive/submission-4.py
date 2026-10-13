class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Brute force
        # Sort the array, then get the + 1 compared to the last element of the array
        nums.sort()
        target =1 
        for i in nums:
            if i == target:
                target +=1
            if i < target:
                continue
            if i >target:
                break
        return target