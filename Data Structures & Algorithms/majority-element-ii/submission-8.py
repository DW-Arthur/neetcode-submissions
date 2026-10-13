from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            
            # When we collect 3 distinct numbers, cancel 1 from all three
            if len(counter) > 2:
                new_counter = {}
                for cand, count in counter.items():
                    if count - 1 > 0:
                        new_counter[cand] = count - 1
                counter = new_counter

        # Second pass: verify survivors
        return [cand for cand in counter if nums.count(cand) > len(nums) // 3]