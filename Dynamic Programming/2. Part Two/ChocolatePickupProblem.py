class Solution:
    def maxChocolate(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        
        # def helper(i, j1, j2):
        #     if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
        #         return float('-inf')

        #     if i == n-1:
        #         if j1 != j2:
        #             return grid[i][j1] + grid[i][j2]
        #         else:
        #             return grid[i][j1]

        #     maxi = float('-inf')

        #     for dj1 in range(-1, 2):
        #         for dj2 in range(-1, 2):

        #             if j1 == j2:
        #                 value = grid[i][j1]
        #             else:
        #                 value = grid[i][j1] + grid[i][j2]

        #             value += helper(i+1, j1+dj1, j2+dj2)

        #             maxi = max(maxi, value)

        #     return maxi
        
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1]*m for _ in range(m)] for _ in range(n)]

        def helper(i, j1, j2):

            if j1 < 0 or j2 < 0 or j1 >= m or j2 >= m:
                return float('-inf')

            if dp[i][j1][j2] != -1:
                return dp[i][j1][j2]

            if i == n-1:
                if j1 != j2:
                    return grid[i][j1] + grid[i][j2]
                else:
                    return grid[i][j1]

            maxi = float('-inf')

            for dj1 in range(-1, 2):
                for dj2 in range(-1, 2):

                    if j1 == j2:
                        value = grid[i][j1]
                    else:
                        value = grid[i][j1] + grid[i][j2]

                    value += helper(i+1, j1+dj1, j2+dj2)

                    maxi = max(maxi, value)

            dp[i][j1][j2] = maxi
            return maxi

        return helper(0, 0, m-1)        
        
        
            