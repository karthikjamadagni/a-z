class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0

        for i in range(n):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                area = height * (i - index)
                maxArea = max(area, maxArea)
                start = index

            stack.append((start, heights[i]))


        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))

        return maxArea
            