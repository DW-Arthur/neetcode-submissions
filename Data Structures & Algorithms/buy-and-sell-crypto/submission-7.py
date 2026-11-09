class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        result =0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                result = max(result, prices[j]- prices[i])
        return result