class Solution:
    def maxLength(self, arr):
        # code here
        prefix_sum = 0
        index_map = {0: -1}
        max_length = 0
        
        for i, num in enumerate(arr):
            prefix_sum += num
            
            if prefix_sum in index_map:
                length = i - index_map[prefix_sum]
                max_length = max(max_length, length)
                
            else:
                index_map[prefix_sum] = i
                
        return max_length