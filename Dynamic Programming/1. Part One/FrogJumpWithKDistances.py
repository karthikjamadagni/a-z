def frogjumpwithKdistances(height, k):
    n = len(height)
    memo = {}

    def helper(i):
        if i == 0:
            return 0

        if i in memo:
            return memo[i]

        minCost = float('inf')

        for j in range(1, k+1):
            if i - j >= 0:
                cost = helper(i-j) + abs(height[i] - height[i-j])
                minCost = min(minCost, cost)

        memo[i] = minCost
        return memo[i]

    return helper(n-1)