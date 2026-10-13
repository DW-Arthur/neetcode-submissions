class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Brute force, the counter method/
        # This is not O(1)
        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0
            counter[i] += 1
        sorted_keys = sorted(counter, key=counter.get)
        print(counter)
        return sorted_keys[-1]
            
        