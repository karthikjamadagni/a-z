# def helper(i, j, count):
#     if i < 0 or j < 0:
#         return count

#     res = count

#     if s1[i] == s2[j]:
#         res = helper(i - 1, j - 1, count + 1)

#     option1 = helper(i - 1, j, 0)
#     option2 = helper(i, j - 1, 0)

#     return max(res, option1, option2)


# a = len(s1)
# b = len(s2)

# res = helper(a - 1, b - 1, 0)
# print(res)

# ------------- BRUTE FORCE --------------


def longest_common_substring(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    ans = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0

    return ans


# Example
s1 = "ABABC"
s2 = "BABCA"

res = longest_common_substring(s1, s2)
print(res)