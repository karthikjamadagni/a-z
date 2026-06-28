class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def helper(start, end):
            memo = {}

            def dp(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                rob = nums[i] + dp(i+2)
                skip = dp(i+1)

                memo[i] = max(rob, skip)
                return memo[i]

            return dp(start)

        if n == 1:
            return nums[0]

        case1 = helper(0, n-2)
        case2 = helper(1, n-1)

        return max(case1, case2)