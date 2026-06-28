class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        # def helper(row, col):
        #     if row == 0 and col == 0:
        #         return 1

        #     if row < 0 or col < 0:
        #         return 0

        #     up, left = 0, 0

            # if obstacleGrid[row][col-1] != 1:
            #     left = helper(row, col-1)

            # if obstacleGrid[row-1][col] != 1:
            #     up = helper(row-1, col)

        #     return left + up

        # return helper(n-1, m-1)

        # recursive solution . PS: I'm a genius you know

        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = 1
        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]

        return dp[n-1][m-1]