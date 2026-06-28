class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum %2 != 0:
            return False
        else:
            return self.sumpossible(nums, nums_sum//2)


    def sumpossible(self, nums:List[int], target) -> bool:

        n = len(nums)
        m = target

        t = [[False] * (m + 1) for _ in range(n + 1)]

        for i in range(n+1):
            t[i][0] = True


        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums[i-1] <= j:
                    t[i][j] = t[i-1][j] or t[i-1][j-nums[i-1]]

                else:
                    t[i][j] = t[i-1][j]


        return t[n][m]




