class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # def helper(i, j):
        #     if i == 0 or j == 0:
        #         return 0

        #     if s1[i-1] == s2[j-1]:
        #         res = 1 + helper(i-1, j-1)
        #         return res

        #     else:
        #         option1 = helper(i-1, j)
        #         option2 = helper(i, j-1)
        #         return max(option1, option2)

        # s1 = s
        # s2 = s1[::-1]

        # n = len(s)
        # return helper(n, n)
        s1 = s
        s2 = s1[::-1]
        n = len(s1)
        m = n
        dp = [[0 for j in range(n+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = 0

        for j in range(m+1):
            dp[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    res = 1 + dp[i-1][j-1]
                    dp[i][j] = res

                else:
                    option1 = dp[i-1][j]
                    option2 = dp[i][j-1]
                    dp[i][j] = max(option1, option2)

        return dp[n][n]