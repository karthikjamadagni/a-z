class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # def helper(row, col):
        #     if row == 0 and col == 0:
        #         return grid[0][0]

        #     left, up = float('inf'), float('inf')
        #     if col > 0:
        #         left = helper(row, col-1)
        #     if row > 0:
        #         up = helper(row-1, col)

        #     return min(grid[row][col]+left, grid[row][col]+up)

        # return helper(len(grid)-1, len(grid[0])-1)

        # in the above case, we are returning float('inf') because we are trying to minimize. I'm fucking fool
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        dp[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue

                left, up = float('inf'), float('inf')
                if j > 0:
                    left = dp[i][j-1]

                if i > 0:
                    up = dp[i-1][j]

                dp[i][j] = min(grid[i][j]+left, grid[i][j]+up)

        return dp[n-1][m-1]
        