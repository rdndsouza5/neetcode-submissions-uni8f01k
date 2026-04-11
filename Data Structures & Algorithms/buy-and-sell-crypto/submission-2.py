class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,profit=prices[0],0
        for i in prices:
            low = min(low,i)

            profit =max(profit,i-low)
        return profit