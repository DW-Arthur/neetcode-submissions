class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            if nums[i] == val:
                # Replace current item with the last available item
                nums[i] = nums[n - 1]
                # Reduce size of the valid array
                n -= 1
            else:
                # Only move forward if current item is valid
                i += 1
                
        return n