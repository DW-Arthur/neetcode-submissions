class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # In this problem, the second you see a value higher than the current, get the 
        # difference, since holding through multiple days for higher value will result
        # in lower value]
        # Do I need left and right pointer?
        result = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                continue
            result += prices[i] - prices[i-1]
        return result

        