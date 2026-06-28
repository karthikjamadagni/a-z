class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # def helper(index, buy, cap):
        #     if cap == 2:
        #         return 0
        #     if index == n:
        #         return 0

        #     profit = 0
        #     if buy:
        #         profit = max(-prices[index] + helper(index+1, False, cap), helper(index+1, True, cap))
        #     else:
        #         profit = max(prices[index] + helper(index+1, True, cap+1), helper(index+1, False, cap))

        #     return profit


        # n = len(prices)
        # return helper(0, True, 0)

        # --------------------------- tabulation -----------------------------------------
        n = len(prices)
        dp = [[[0 for k in range(3)] for j in range(2)] for i in range(n+1)]

        for index in range(n-1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 1:
                        dp[index][buy][cap] = max(-prices[index] + dp[index+1][0][cap], dp[index+1][1][cap])

                    else:
                        dp[index][buy][cap] = max(prices[index] + dp[index+1][1][cap-1], dp[index+1][0][cap])    

        return dp[0][1][2]