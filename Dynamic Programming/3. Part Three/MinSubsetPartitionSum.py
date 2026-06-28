class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        k = sum(nums)
        n = len(nums)

        dp = [[False] * (k + 1) for _ in range(n)]

        # Sum 0 is always possible
        for i in range(n):
            dp[i][0] = True

        # First element
        if nums[0] <= k:
            dp[0][nums[0]] = True

        # Fill DP table
        for i in range(1, n):
            for j in range(1, k + 1):

                not_take = dp[i - 1][j]

                take = False
                if nums[i] <= j:
                    take = dp[i - 1][j - nums[i]]

                dp[i][j] = take or not_take

        # Find minimum difference
        ans = float('inf')

        for s1 in range(k // 2 + 1):
            if dp[n - 1][s1]:
                s2 = k - s1
                ans = min(ans, abs(s2 - s1))

        return ans