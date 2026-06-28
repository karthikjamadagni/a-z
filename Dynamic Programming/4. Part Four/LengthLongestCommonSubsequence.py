class Solution:
    def lcs(self, s1, s2):
        # code here
        
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
                
            if s1[i] == s2[j]:
                res = 1 + helper(i-1, j-1)
                return res
                
            option1 = helper(i-1, j)
            option2 = helper(i, j-1)
            
            res = max(option1, option2)
            
            return res
            
        a = len(s1)
        b = len(s2)
        
        res = helper(a-1, b-1)
        return res
        # n = len(s1)
        # m = len(s2)
        # dp = [[0 for j in range(m+1)] for _ in range(n+1)]
        
        # for i in range(n+1):
        #     dp[i][0] = 0
            
        # for j in range(m+1):
        #     dp[0][j] = 0
            
            
        # for i in range(1, n+1):
        #     for j in range(1, m+1):
        #         if s1[i-1] == s2[j-1]:
        #             res = 1 + dp[i-1][j-1]
        #             dp[i][j] = res
                    
        #         else:
        #             option1 = dp[i-1][j]
        #             option2 = dp[i][j-1]
                    
        #             res = max(option1, option2)
                    
        #             dp[i][j] = res
                
        # return dp[n][m]
        
        
            
        
        