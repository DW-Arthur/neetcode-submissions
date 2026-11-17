class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute force, for each window, check for the max number
        result = []
        left =0
        for right in range(k-1, len(nums)):
            # Go through each window
            current = float('-inf')
            #left = 0, right = k-1
            for i in range(left, right+1):
                current = max(current, nums[i])
            result.append(current)
            left +=1
        return result
