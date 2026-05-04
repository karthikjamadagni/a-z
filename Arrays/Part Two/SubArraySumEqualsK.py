class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = {0: 1}
        curSum = 0
        count = 0

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k

            count += prefix_dict.get(diff, 0)

            prefix_dict[curSum] = 1 + prefix_dict.get(curSum, 0)


        return count
