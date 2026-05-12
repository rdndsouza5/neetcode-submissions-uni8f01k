class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        curProfit = 0
        
        for i in prices:
            if i  < curMin:
                curMin = i
            if i > curMin:
                curProfit += i - curMin
                curMin = i
        return curProfit