class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The max daily eaten bananas is the max number in the arrray
        # Do binary search between 1 and max num
        maxNum = -1
        for i in piles:
            maxNum = max(maxNum, i)
        left, right = 1, maxNum
        result = right
        while left<=right:
            mid = (left + right) //2
            # Find out the eating speed
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / mid)
            if totalTime > h:
                left = mid +1
            elif totalTime <= h:
                right = mid -1
                result = mid
        return result

        