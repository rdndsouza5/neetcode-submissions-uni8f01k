class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        maxP = prices[0]
        res = 0
        for i in prices:
            minP = min(minP, i)
            res = max(res, i-minP)
        return res