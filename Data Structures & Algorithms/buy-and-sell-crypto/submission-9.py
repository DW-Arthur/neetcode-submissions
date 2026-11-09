class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Sliding Window
        # 10 11 12 13  2000000
        # L R
        #   LR
        #      
        left, right =0,1 
        result = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left +=1
            else:
                result = max(result, prices[right]- prices[left])
                right +=1
        return result