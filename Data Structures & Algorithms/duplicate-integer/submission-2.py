class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Dict uses key value pairs
        match = {}
        for i in nums:
            if i in match:
                return True
            match[i] = i
        return False
         