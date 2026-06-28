# class Solution:
#     def maximumPoints(self, mat):
#         n = len(mat)

#         def solve(day, last):
#             if day == 0:
#                 maxi = 0
#                 for task in range(3):
#                     if task != last:
#                         maxi = max(maxi, mat[0][task])
#                 return maxi

#             maxi = 0
#             for task in range(3):
#                 if task != last:
#                     points = mat[day][task] + solve(day - 1, task)
#                     maxi = max(maxi, points)

#             return maxi

#         return solve(n - 1, 3)

# ------------------------------ BRUTE FORCE  --------------------------------------------


# class Solution:
#     def maximumPoints(self, mat):
#         n = len(mat)

#         dp = [[-1] * 4 for _ in range(n)]

#         def solve(day, last):
#             if dp[day][last] != -1:
#                 return dp[day][last]

#             if day == 0:
#                 maxi = 0
#                 for task in range(3):
#                     if task != last:
#                         maxi = max(maxi, mat[0][task])

#                 dp[0][last] = maxi
#                 return maxi

#             maxi = 0
#             for task in range(3):
#                 if task != last:
#                     points = mat[day][task] + solve(day - 1, task)
#                     maxi = max(maxi, points)

#             dp[day][last] = maxi
#             return maxi

#         return solve(n - 1, 3)



# ------------------------------ Memoization ------------------------------------------






class Solution:
    def maximumPoints(self, mat):
        n = len(mat)

        dp = [[0]*4 for _ in range(n)]

        dp[0][0] = max(mat[0][1], mat[0][2])
        dp[0][1] = max(mat[0][0], mat[0][2])
        dp[0][2] = max(mat[0][0], mat[0][1])
        dp[0][3] = max(mat[0])

        for i in range(1, n):
            for last in range(4):
                dp[i][last] = 0

                for task in range(3):
                    if task != last:
                        points = mat[i][task] + dp[i-1][task]
                        dp[i][last] = max(dp[i][last], points)

        return dp[n-1][3]


# ------------------------------ Tabulation ------------------------------------------------




# class Solution:
#     def maximumPoints(self, mat):
#         n = len(mat)

#         prev = [0] * 4

#         # Base case (day 0)
#         prev[0] = max(mat[0][1], mat[0][2])
#         prev[1] = max(mat[0][0], mat[0][2])
#         prev[2] = max(mat[0][0], mat[0][1])
#         prev[3] = max(mat[0])

#         # Process remaining days
#         for day in range(1, n):
#             curr = [0] * 4

#             for last in range(4):
#                 curr[last] = 0

#                 for task in range(3):
#                     if task != last:
#                         curr[last] = max(
#                             curr[last],
#                             mat[day][task] + prev[task]
#                         )

#             prev = curr

#         return prev[3]


# -------------------- Space Optimization ----------------------------------------------