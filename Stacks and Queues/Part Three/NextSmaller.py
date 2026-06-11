class Solution:
    def nextSmallerEle(self, arr):
        # code here
        n = len(arr)
        i = n - 1
        
        stack = []
        answer = [-1] * n
        
        while (i >= 0):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
                
            if stack:
                answer[i] = stack[-1]
                
            stack.append(arr[i])
                
                
            i -= 1

        return answer