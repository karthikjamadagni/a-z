class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arr_sum = sum(nums)

        cum_sum = 0

        for i in range(n+1):
            cum_sum += i

        # The below thing can be used to optimize
        #expected = n * (n + 1) // 2


        return cum_sum - arr_sum