class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0

        while i < n:
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1

            nums[j] = nums[i]
            j += 1
            i += 1

        return j