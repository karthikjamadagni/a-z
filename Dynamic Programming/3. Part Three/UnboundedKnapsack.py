class Solution:
    def knapSack(self, val, wt, capacity):
        # code here
        n = len(wt)
        
        # def helper(index, cl): # capacity left in the bag
        #     if index == 0:
        #         if wt[0] <= cl:
        #             return val[0]
                    
        #         else:
        #             return 0
                    
            
        #     not_take = 0 + helper(index-1, cl)
        #     take = float('-inf')
        #     if cl >= wt[index]:
        #         take = val[index] + helper(index, cl-wt[index])
                
        #     return max(take, not_take)
            
        # return helper(n-1, capacity)
        
        dp = [[0 for j in range(capacity+1)] for _ in range(n)]
        
        for i in range(capacity+1):
            if wt[0] <= i:
                dp[0][i] = (i // wt[0]) * val[0]
                
            else:
                dp[0][i] = 0
                
                
        for index in range(1, n):
            for cl in range(0, capacity+1):
                not_take = 0 + dp[index-1][cl]
                take = float('-inf')
                if cl >= wt[index]:
                    take = val[index] + dp[index][cl-wt[index]]
                    
                dp[index][cl] = max(take, not_take)
                
        return dp[n-1][capacity]
        