from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = {}
        
        for num in nums:
            # 1. Existing candidate: simply increment
            if num in counter:
                counter[num] += 1
            # 2. Free slot available: add new candidate
            elif len(counter) < 2:
                counter[num] = 1
            # 3. 3rd distinct number arrives: cancel 1 from existing candidates
            else:
                # Decrement counts
                for cand in counter:
                    counter[cand] -= 1
                
                # Delete keys that dropped to 0 safely (list copy avoids mutation errors)
                zero_keys = [cand for cand, count in counter.items() if count == 0]
                for k in zero_keys:
                    del counter[k]
        print(counter)
        # Verification pass: count actual frequencies in nums, not in counter
        result = []
        for cand in counter:
            if nums.count(cand) > len(nums) // 3:
                result.append(cand)
                
        return result