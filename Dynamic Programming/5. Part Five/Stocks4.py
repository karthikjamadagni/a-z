class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # def helper(index, buy, cap):
        #     if cap == k:
        #         return 0
        #     if index == n:
        #         return 0

        #     profit = 0
        #     if buy == 1:
        #         return max(-prices[index] + helper(index+1, 0, cap), #buy
        #                     helper(index+1, 1, cap)   # skip
        #                     )

        #     else:
        #         return max(prices[index] + helper(index+1, 1, cap+1),
        #                 helper(index+1, 0, cap)
        #         )

        #     return profit
        # n = len(prices)
        # return helper(0, 1, 0)
        

        n = len(prices)
        dp = [[[0 for l in range(k+1)] for j in range(2)] for i in range(n+1)]

        for index in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
                    if buy == 1:
                        dp[index][buy][cap] =  max(-prices[index] + dp[index+1][0][cap], #buy
                                    dp[index+1][1][cap]   # skip
                                    )

                    else:
                        dp[index][buy][cap] =  max(prices[index] + dp[index+1][1][cap-1],
                                dp[index+1][0][cap]
                        )


        return dp[0][1][k]