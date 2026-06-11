class Solution:
    def isValid(self, s: str) -> bool:
        closing_brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []

        for char in s:
            if char in closing_brackets.values():
                stack.append(char)

            elif char in closing_brackets:
                if not stack or closing_brackets[char] != stack.pop():
                    return False


        if len(stack) == 0:
            return True
        else:
            return False