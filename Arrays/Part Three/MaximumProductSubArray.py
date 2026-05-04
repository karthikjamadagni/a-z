class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = 1
        suffix = 1

        maximum = float("-inf")

        n = len(nums)

        for i in range(n):
            if prefix == 0:
                prefix = 1
            elif suffix == 0:
                suffix = 1
            prefix = prefix * nums[i]
            suffix = suffix * nums[n-i-1]

            maximum = max(maximum, max(prefix, suffix))


        return maximum

            
