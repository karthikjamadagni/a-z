# def subsetSumToK(n, k, arr):

#     def solve(ind, target):
#         # Base cases
#         if target == 0:
#             return True

#         if ind == 0:
#             return arr[0] == target

#         # Don't take the current element
#         not_take = solve(ind - 1, target)

#         # Take the current element
#         take = False
#         if arr[ind] <= target:
#             take = solve(ind - 1, target - arr[ind])

#         return take or not_take

#     return solve(n - 1, k)


# ---------------- BRUTE FORCE -------------------------



def subsetSumToK(n, k, arr):
    # DP table
    dp = [[False] * (k + 1) for _ in range(n)]

    # Target = 0 is always possible (empty subset)
    for i in range(n):
        dp[i][0] = True

    # First element initialization
    if arr[0] <= k:
        dp[0][arr[0]] = True

    # Fill the DP table
    for ind in range(1, n):
        for target in range(1, k + 1):

            not_take = dp[ind - 1][target]

            take = False
            if arr[ind] <= target:
                take = dp[ind - 1][target - arr[ind]]

            dp[ind][target] = take or not_take

    return dp[n - 1][k]

