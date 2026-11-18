class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = cost[-1], 0
        n = len(cost)
        for i in range(n - 2, -1, -1):
            cost[i] = min(one + cost[i], two + cost[i])
            two = one
            one = cost[i]
        
        return min(cost[0], cost[1])