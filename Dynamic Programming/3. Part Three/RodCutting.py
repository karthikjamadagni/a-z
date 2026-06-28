#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        
        n = len(price)
        
        # def helper(index, length): # il - > inches left
        #     if index == 0:
        #         return length * price[0]
                
        #     not_take = 0 + helper(index-1, length)
        #     take = 0
            
        #     rod_length = index + 1
        #     if length >= rod_length:
        #         take = price[index] + helper(index, length - rod_length)
                
        #     return max(take, not_take)
            
        # return helper(n-1, n)
        
        
        dp = [[0 for j in range(n+1)] for _ in range(len(price))]
        
        for i in range(n+1):
            dp[0][i] = i * price[0]
        
        for index in range(1, n):
            for length in range(0, n+1):
                not_take = 0 + dp[index-1][length]
                take = 0
                
                rod_length = index + 1
                if length >= rod_length:
                    take = price[index] + dp[index][length - rod_length]
                    
                dp[index][length] = max(take, not_take)
                
        return dp[n-1][n]
        