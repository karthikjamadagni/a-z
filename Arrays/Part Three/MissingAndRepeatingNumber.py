class Solution:
    def findTwoElement(self, arr):
        # code here
        arr_sum = sum(arr)
        n = len(arr)
        
        num_set = set()
        repeating_number = 0
        
        for i in range(n):
            if arr[i] in num_set:
                repeating_number = arr[i]
            num_set.add(arr[i])
            
        unique_sum = sum(num_set)
        expected_sum = (n * (n+1)) // 2
        
        missing_number = expected_sum - unique_sum
        
        return [repeating_number, missing_number]
            
        
        
        
