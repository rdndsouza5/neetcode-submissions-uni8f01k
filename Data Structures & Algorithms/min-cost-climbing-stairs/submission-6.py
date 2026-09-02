class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=1:
            return 0
        prev, cur = cost[0], cost[1]

        for i in range(2, len(cost)):
            val = min(prev, cur)+ cost[i]
            prev = cur
            cur = val
        return min(cur, prev)
            