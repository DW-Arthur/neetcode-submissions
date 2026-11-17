from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Stores INDICES, kept in strictly decreasing order of nums[index]
        result = []
        left = 0

        for right in range(len(nums)):
            # 1. Maintain decreasing order:
            # Pop indices from the back whose values are smaller than the incoming nums[right]
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # 2. Add current index to the back
            q.append(right)

            # 3. Remove expired front index if it fell outside the left boundary
            if q[0] < left:
                q.popleft()

            # 4. Once our window hits size k (right >= k - 1), record max and slide left
            if right >= k - 1:
                result.append(nums[q[0]])
                left += 1

        return result