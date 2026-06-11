class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = []
        n = len(nums)

        i = 2 * n - 1

        while ( i >= 0):
            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if not stack:
                    answer.append(-1)

                else:
                    answer.append(stack[-1])

            stack.append(nums[i%n])
            i -= 1


        i = 0
        j = len(answer)-1

        while i < j:
            temp = answer[i]
            answer[i] = answer[j]
            answer[j] = temp

            i += 1
            j -= 1

        return answer

        