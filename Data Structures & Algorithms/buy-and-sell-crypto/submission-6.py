class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        least, res = prices[0],0
        for p in prices:
            least = min(least, p)
            res=max(res, p-least)
        return res