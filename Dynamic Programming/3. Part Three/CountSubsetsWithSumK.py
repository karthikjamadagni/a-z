class Solution:
    def perfectSum(self, arr, target):
        n = len(arr)
        dp = [[0 for _ in range(target+1)] for _ in range(n)]

        # sum 0 can always be formed by empty subset
        for i in range(n):
            dp[i][0] = 1

        if arr[0] <= target:
            dp[0][arr[0]] += 1

        for i in range(1, n):
            for j in range(target+1):

                not_take = dp[i-1][j]

                take = 0
                if (j-arr[i] >= 0):
                    take = dp[i-1][j-arr[i]]

                dp[i][j] = take + not_take

        return dp[n-1][target]