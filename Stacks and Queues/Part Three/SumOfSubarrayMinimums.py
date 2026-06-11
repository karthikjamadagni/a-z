class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        nse = [n] * n
        pse = [-1] * n

        def findnse():
            stack = []
            i = n - 1

            while i >= 0:
                while stack and arr[stack[-1]] > arr[i]:
                    stack.pop()

                if stack:
                    nse[i] = stack[-1]

                stack.append(i)
                i -= 1

        def findpse():
            stack = []
            i = 0

            while i < n:
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()

                if stack:
                    pse[i] = stack[-1]

                stack.append(i)
                i += 1

        findnse()
        findpse()

        total = 0
        mod = 10 ** 9 + 7

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i
            total = (total + (left * right * arr[i]) % mod) % mod

        return total