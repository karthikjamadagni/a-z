class Solution:
    def countPartitions(self, arr, diff):
        # code here
        k = sum(arr)
        n = len(arr)
        
        if (k + diff) % 2 != 0:
            return 0
        target = (k + diff) // 2
        dp = [[0 for j in range(target+1)] for _ in range(n)]
        
        
        
        
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
            
        for i in range(1, n):
            for j in range(target+1):
                not_take = dp[i-1][j]
                
                take = 0
                
                if (j-arr[i]) >= 0:
                    take = dp[i-1][j-arr[i]]
                    
                dp[i][j] = take + not_take
                
        return dp[n-1][target]
        
