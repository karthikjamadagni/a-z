class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        prefixSum = [[0] * m for _ in range(n)]
        for j in range(m):
            arr_sum = 0
            for i in range(n):
                arr_sum += int(matrix[i][j])
                if matrix[i][j] == '0':
                    arr_sum = 0
                prefixSum[i][j] = arr_sum

        print(prefixSum)

        def maximumAreaInHistogram(array):
            n = len(array)
            stack = []

            maxArea = 0

            for i in range(n):
                start = i
                while stack and stack[-1][1] > array[i]:
                    index, height = stack.pop()
                    area = height * (i - index)
                    maxArea = max(area, maxArea)
                    start = index
                stack.append((start, array[i]))

            for i, h in stack:
                maxArea = max(maxArea, h * (len(array) - i))

            return maxArea

        maxArea = 0
        for i in range(len(prefixSum)):
            maxArea = max(maxArea, maximumAreaInHistogram(prefixSum[i]))

        return maxArea