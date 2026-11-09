class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The best time to buy a stock 
        # left and right pointer
        # Move the left to the right immediately, since if right < left, it is smaller
        # than all other elements to the right
        left = 0
        result = 0 
        for right in range(len(prices)-1):
            if prices[right] < prices[left]:
                left = right
                right +=1
                continue
            right +=1
            result = max(result, prices[right]-prices[left])
        return result

        