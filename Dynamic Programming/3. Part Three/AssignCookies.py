class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        l, r = 0, 0
        count = 0
        while l < len(s) and r < len(g):
            if s[l] >= g[r]:
                count += 1
                l += 1
                r += 1

            elif s[l] < g[r]:
                l += 1

        return count
