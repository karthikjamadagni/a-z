class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        def helper(index, target):
            if target < 0:
                return 0
            if index == 0:
                if target % coins[0] == 0:
                    return 1
                else:
                    return 0
            take = helper(index, target-coins[index])
            not_take = 0
            if index >= 1:
                not_take = helper(index-1, target)

            return take + not_take

        # return helper(n-1, amount)


        dp = [[0 for j in range(amount+1)] for _ in range(n)]
        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = 1

        for index in range(1, n):
            for target in range(amount+1):
                not_take = dp[index-1][target]
                take = 0
                if target >= coins[index]:
                    take = dp[index][target-coins[index]]
                dp[index][target] = take + not_take
        return dp[n-1][amount]