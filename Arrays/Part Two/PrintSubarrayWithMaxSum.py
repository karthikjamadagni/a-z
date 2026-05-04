class Solution:
    def printMaxSubarray(self, nums):
        ans_start = 0
        ans_end = 0
        
        start = 0
        arr_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Decide: start new or extend
            if nums[i] > arr_sum + nums[i]:
                arr_sum = nums[i]
                start = i
            else:
                arr_sum += nums[i]
            
            # Update answer
            if arr_sum > max_sum:
                max_sum = arr_sum
                ans_start = start
                ans_end = i