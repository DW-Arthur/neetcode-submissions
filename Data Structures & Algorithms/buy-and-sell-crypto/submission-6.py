class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        result = 0

        while r < len(prices):
            if prices[l] < prices[r]:  # valid profit
                result = max(result, prices[r] - prices[l])
                r += 1
            else:
                l += 1
                # 🔑 make sure r is always ahead of l
                if r <= l:
                    r = l + 1
        return result
