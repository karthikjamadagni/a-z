class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for i in range(len(num)):
            while stack and (stack[-1] > num[i]) and k > 0:
                stack.pop()
                k -= 1

            stack.append(num[i])

        while stack and k > 0:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        res = ""
        while stack:
            res = stack.pop() + res

        res = res.lstrip('0')
        if res == "":
            return "0"

        return res