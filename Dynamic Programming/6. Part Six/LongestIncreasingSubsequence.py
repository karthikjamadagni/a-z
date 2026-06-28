# class Solution:
#     def lis(self, arr):
#         n = len(arr)

#         def f(index, prev):
#             # Base case
#             if index == n:
#                 return 0

#             # Option 1: Don't take current element
#             not_take = 0 + f(index + 1, prev)

#             # Option 2: Take current element
#             take = 0
#             if prev == -1 or arr[index] > arr[prev]:
#                 take = 1 + f(index + 1, index)

#             return max(take, not_take)

#         return f(0, -1)

# -------------------------- BRUTE FORCE -------------------



# class Solution:
#     def lis(self, arr):
#         n = len(arr)

#         dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

#         def f(index, prev):
#             # Base case
#             if index == n:
#                 return 0

#             # Memoization
#             if dp[index][prev + 1] != -1:
#                 return dp[index][prev + 1]

#             # Option 1: Don't take
#             not_take = f(index + 1, prev)

#             # Option 2: Take
#             take = 0
#             if prev == -1 or arr[index] > arr[prev]:
#                 take = 1 + f(index + 1, index)

#             dp[index][prev + 1] = max(take, not_take)
#             return dp[index][prev + 1]

#         return f(0, -1)





# ------------------- Memoizaton -----------------------------




# class Solution:
#     def lis(self, arr):
#         n = len(arr)

#         dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

#         # index goes from n-1 to 0
#         for index in range(n - 1, -1, -1):

#             # prev goes from index-1 down to -1
#             for prev in range(index - 1, -2, -1):

#                 # Don't take
#                 not_take = dp[index + 1][prev + 1]

#                 # Take
#                 take = 0
#                 if prev == -1 or arr[index] > arr[prev]:
#                     take = 1 + dp[index + 1][index + 1]

#                 dp[index][prev + 1] = max(take, not_take)

#         return dp[0][0]


# ------------------ Tabulation ----------------------------------







class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []

        def binary_search(num):
            left, right = 0, len(ans)

            while left <= right:
                mid = (left + right) // 2
                if ans[mid] < num:
                    left += 1

                else:
                    right -= 1

            return left

        for num in nums:
            if not ans or ans[-1] < num:
                ans.append(num)

            else:
                index = binary_search(num)
                ans[index] = num

        return len(ans)
    


# Optimal solution 👆