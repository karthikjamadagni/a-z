class Solution:
    def minCost(self, height):
        n = len(height)
        memo = {}

        def helper(i):
            if i == n - 1:
                return 0

            if i in memo:
                return memo[i]

            # jump 1 step
            cost1 = abs(height[i] - height[i+1]) + helper(i+1)

            # jump 2 steps
            cost2 = float('inf')
            if i + 2 < n:
                cost2 = abs(height[i] - height[i+2]) + helper(i+2)

            memo[i] = min(cost1, cost2)
            return memo[i]

        return helper(0)