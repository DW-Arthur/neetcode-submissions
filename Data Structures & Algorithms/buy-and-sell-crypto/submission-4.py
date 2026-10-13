class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        left, right = 0,1 
        while left < right and right < len(prices):
            if prices[left] >= prices[right]:
                left = right
                right +=1
            else:
                result = max(result, prices[right]- prices[left])
                right +=1
                # prices=[5,1,5,6,7,1,10]
                # Wrong result, since at the last 2 indexes, the right will keep incresing
                # just move the left to right, since left are already smaller than
        return result
