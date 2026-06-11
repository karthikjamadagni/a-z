from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:

        n = len(nums)
        pse = [-1] * n          # previous smaller index
        nse = [n] * n           # next smaller index
        pge = [-1] * n          # previous greater index
        nge = [n] * n           # next greater index
        
        def findpse():
            stack = []
            i = 0
            while i < n:
                while stack and nums[stack[-1]] > nums[i]:
                    stack.pop()

                if stack:
                    pse[i] = stack[-1]

                stack.append(i)
                i += 1

        def findnse():
            stack = []
            i = n - 1
            while i >= 0:
                while stack and nums[stack[-1]] >= nums[i]:
                    stack.pop()

                if stack:
                    nse[i] = stack[-1]

                stack.append(i)
                i -= 1

        def findnge():
            stack = []
            i = n - 1
            while i >= 0:
                while stack and nums[stack[-1]] <= nums[i]:
                    stack.pop()

                if stack:
                    nge[i] = stack[-1]

                stack.append(i)
                i -= 1

        def findpge():
            stack = []
            i = 0
            while i < n:
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()

                if stack:
                    pge[i] = stack[-1]

                stack.append(i)
                i += 1

        findpse()
        findnse()
        findpge()
        findnge()

        ssmn = 0
        ssmx = 0

        for i in range(n):
            # contribution as minimum
            left_min = i - pse[i]
            right_min = nse[i] - i
            ssmn += left_min * right_min * nums[i]

            # contribution as maximum
            left_max = i - pge[i]
            right_max = nge[i] - i
            ssmx += left_max * right_max * nums[i]

        return ssmx - ssmn
