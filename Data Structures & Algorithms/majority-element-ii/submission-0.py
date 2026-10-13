class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Brute Force
        counter = {}
        result = []
        for i in nums:
            if i not in counter:
                counter[i] =0
            counter[i] +=1
        for key, value in counter.items():
            if value > len(nums)/3:
                result.append(key)
        return result