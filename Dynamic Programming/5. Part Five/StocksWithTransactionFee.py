class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # n = len(prices)
        # def helper(index, buy):
        #     if index == n:
        #         return 0

        #     profit = 0
        #     if buy == 1:
        #         profit = max(-prices[index] + helper(index+1, 0), helper(index+1, 1))

        #     else:
        #         profit = max(prices[index] - fee + helper(index+1, 1), helper(index+1, 0))

        #     return profit

        # return helper(0, 1)


        # ----------------------- tabulation -------------------------------
        n = len(prices)
        dp = [[0 for j in range(2)] for i in range(n+1)]

        for index in range(n-1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    dp[index][buy] = max(-prices[index] + dp[index+1][0], dp[index+1][1])
                else:
                    dp[index][buy] = max(prices[index] - fee + dp[index+1][1], dp[index+1][0])

        return dp[0][1]