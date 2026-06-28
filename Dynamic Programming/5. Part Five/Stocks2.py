class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # def helper(index, buy):
        #     if index == n:
        #         return 0

        #     profit = 0
        #     if buy:
        #         profit = max(-prices[index] + helper(index+1, False), helper(index+1, True))
        #     else:
        #         profit = max(prices[index] + helper(index+1, True), helper(index+1, False))

        #     return profit


        # n = len(prices)
        # return helper(0, True)


        # ---------------------------------- tabulation -----------------------------------
        n = len(prices)
        
        # dp[i][buy] -> max profit from index i with buy state
        dp = [[0 for _ in range(2)] for _ in range(n + 1)]

        # Base case: dp[n][0] = dp[n][1] = 0 (already initialized)

        for i in range(n - 1, -1, -1):
            for buy in range(2):
                if buy:
                    dp[i][1] = max(-prices[i] + dp[i + 1][0],# buy
                        dp[i + 1][1]               # skip
                    )
                else:
                    dp[i][0] = max(
                        prices[i] + dp[i + 1][1],  # sell
                        dp[i + 1][0]               # skip
                    )

        return dp[0][1]
