# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)
    

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = {}

#         def dfs(k):
#             if k <= 2:
#                 return k

#             if k in memo:
#                 return memo[k]

#             memo[k] = dfs(k - 1) + dfs(k - 2)
#             return memo[k]

#         return dfs(n)


# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         dp = [0] * (n + 1)

#         dp[1] = 1
#         dp[2] = 2

#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]

#         return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        
        prev2 = 1
        prev1 = 2
        current = 0

        for i in range(3, n+1):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current
        return current