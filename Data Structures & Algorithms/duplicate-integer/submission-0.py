class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = []
        for i in nums:
            if i in test:
                return True
            test.append(i)
        return False
         