class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        nums_set = set()
        for i in range(n):
            nums_set.add(nums[i])

        longest = 0

        for num in nums_set:
            if num-1 not in nums_set:
                current = num
                streak = 1

                while current+1 in nums_set:
                    streak += 1
                    current += 1

                longest = max(longest, streak)


        return longest
