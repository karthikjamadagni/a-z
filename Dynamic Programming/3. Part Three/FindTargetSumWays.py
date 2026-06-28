class Solution:
    def findTargetSumWays(self, nums: List[int], target: int):

        n = len(nums)
        k = sum(nums)

        # Impossible cases
        if abs(target) > k:
            return 0

        if (k + target) % 2 != 0:
            return 0

        k = (k + target) // 2

        dp = [[0] * (k + 1) for _ in range(n)]

        # Base case
        if nums[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1

        if nums[0] != 0 and nums[0] <= k:
            dp[0][nums[0]] = 1

        for i in range(1, n):
            for j in range(k + 1):

                not_take = dp[i - 1][j]

                take = 0
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]

                dp[i][j] = take + not_take

        print(dp)

        return dp[n - 1][k]