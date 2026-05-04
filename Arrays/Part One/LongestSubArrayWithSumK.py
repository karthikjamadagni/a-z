class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_map = {}
        
        prefix_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                max_length = i + 1
                
            if prefix_sum - k in prefix_map:
                length  = i - prefix_map[prefix_sum - k]
                max_length = max(max_length, length )
                
                
            if prefix_sum not in prefix_map:
                prefix_map[prefix_sum] = i
                
                
        return max_length