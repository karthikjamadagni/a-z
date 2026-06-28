class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # This is my code below for recursive s
        # self.minCount = float('inf')
        # def helper(index, target, count):
        #     if target == 0:
        #         self.minCount = min(self.minCount, count)
        #         return

        #     if target < 0 or index > (len(coins)-1):
        #         return

        #     helper(index, target-coins[index], count+1)
        #     helper(index+1, target, count)

        # helper(0, amount, 0)
        # return self.minCount if self.minCount != float('inf') else -1


        # striver's code recursive
        # n = len(coins)
        # def helper(index, target):
        #     if index == 0:
        #         if target % coins[0] == 0:
        #             return target / coins[0]

        #         else:
        #             return float('inf')

        #     not_take = 0 + helper(index-1, target)
        #     take = float('inf')

        #     if coins[index] <= target:
        #         take = 1 + helper(index , target-coins[index])

        #     return min(take, not_take)

        # res = helper(n-1, amount)
        # return int(res) if res != float('inf') else -1 

        # tablulation
        n = len(coins)

        dp = [[float('inf') for j in range(amount+1)] for _ in range(n)]

        for t in range(0, amount+1):
            if t % coins[0] == 0:
                dp[0][t] = int(t / coins[0])

        for index in range(1, n):
            for t in range(0, amount+1):
                not_take = 0 + dp[index-1][t]
                take = float('inf')

                if coins[index] <= t:
                    take = 1 + dp[index][t-coins[index]]

                dp[index][t] = min(take, not_take)

        return dp[n-1][amount] if dp[n-1][amount] != float('inf') else -1
            