class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force, using nested loop to do it 
        # At each index, calculate the max profit by iterating the array
        # Then somehow add the max together
        result = 0
        for i in range(0,len(prices)):
            if i+1<len(prices):
                if prices[i+1] <= prices[i]:
                    # reset
                    continue
                else:
                    result += prices[i+1] - prices[i]
        return result
