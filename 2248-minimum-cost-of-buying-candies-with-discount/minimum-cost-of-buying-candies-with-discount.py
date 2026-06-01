class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        t=0
        for i in range(len(cost)):
            if i%3!=2:
                t+=cost[i]
        return t