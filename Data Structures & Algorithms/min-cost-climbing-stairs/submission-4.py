class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if (len(cost) == 2): return min(cost)
        if len(cost) == 3:
            return min(cost[0] + cost[2], cost[1])
        twoAway = cost[0]
        oneAway = cost[1]
        total = 0

        for cst in range(2, len(cost)):
            total = cost[cst] + min(twoAway, oneAway)
            twoAway = oneAway
            oneAway = total

        return min(total, twoAway)