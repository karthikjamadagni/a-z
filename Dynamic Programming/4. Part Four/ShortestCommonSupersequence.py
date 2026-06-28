# n = len(s1)
# m = len(s2)

#len (shortest common supersequence of s1 and s2) = n + m - lcs(s1 and s2)

# just print it


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        dp = [[0 for j in range(m+1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 0

        for j in range(m+1):
            dp[0][j] = 0

        for i in range(1, n+1):
            for j in range(1, m+1):
                if str1[i-1] == str2[j-1]:
                    res = 1 + dp[i-1][j-1]
                    dp[i][j] = res

                else:
                    option1 = dp[i-1][j]
                    option2 = dp[i][j-1]
                    dp[i][j] = max(option1, option2)

        i, j = n, m

        ans = ""

        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                ans += str1[i-1]
                i -= 1
                j -= 1

            elif dp[i-1][j] > dp[i][j-1]:
                ans += str1[i-1]
                i -= 1

            else:
                ans += str2[j-1]
                j -= 1

        while i > 0:
            ans += str1[i-1]
            i -= 1

        while j > 0:
            ans += str2[j-1]
            j -= 1

        return ans[::-1]
    
# The difference between printing this and lcs is that if the characters doesn't match, we add it in this problem
# If the characters match, we add only once
