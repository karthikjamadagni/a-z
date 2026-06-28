# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)

#         def solve(i, j):
#             if i == n - 1:
#                 return triangle[i][j]

#             down = triangle[i][j] + solve(i + 1, j)
#             diagonal = triangle[i][j] + solve(i + 1, j + 1)

#             return min(down, diagonal)

#         return solve(0, 0)

# ----------------------- BRUTE FORCe---------------------------



# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)

#         dp = [[-1] * n for _ in range(n)]

#         def solve(i, j):
#             if i == n - 1:
#                 return triangle[i][j]

#             if dp[i][j] != -1:
#                 return dp[i][j]

#             down = triangle[i][j] + solve(i + 1, j)
#             diagonal = triangle[i][j] + solve(i + 1, j + 1)

#             dp[i][j] = min(down, diagonal)
#             return dp[i][j]

#         return solve(0, 0)



# --------------------- Memoization -----------------------------


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)

#         dp = [[0] * n for _ in range(n)]

#         for j in range(n):
#             dp[n - 1][j] = triangle[n - 1][j]

#         for i in range(n - 2, -1, -1):
#             for j in range(i + 1):
#                 down = triangle[i][j] + dp[i + 1][j]
#                 diagonal = triangle[i][j] + dp[i + 1][j + 1]

#                 dp[i][j] = min(down, diagonal)

#         return dp[0][0]



# --------------------- Tabulation -----------------------------


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)

#         prev = triangle[-1][:]

#         for i in range(n - 2, -1, -1):
#             curr = [0] * (i + 1)

#             for j in range(i + 1):
#                 down = triangle[i][j] + prev[j]
#                 diagonal = triangle[i][j] + prev[j + 1]

#                 curr[j] = min(down, diagonal)

#             prev = curr

#         return prev[0]


# ----------------- Space Optimization --------------------------