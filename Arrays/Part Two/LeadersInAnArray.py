class Solution:
    def leaders(self, arr):
        # code here
        n = len(arr)
        max_peak = arr[n-1]
        
        res = []
        res.append(max_peak)
        
        for i in range(n-2, -1, -1):
            if arr[i] >= max_peak:
                max_peak = arr[i]
                res.append(arr[i])
                
        return reversed(res)
                