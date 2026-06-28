class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # def helper(row, col):
        #     if row == 0 and col == 0:
        #         return 1

        #     if row < 0 or col < 0:
        #         return 0

        #     left = helper(row, col-1)
        #     up = helper(row-1, col)

        #     return left + up

        # above is recursive which is being converted to tabulation

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                up = dp[i-1][j]
                left = dp[i][j-1]

                dp[i][j] = left + up

        return dp[m-1][n-1]