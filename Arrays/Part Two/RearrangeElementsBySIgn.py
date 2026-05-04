class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        pos_idx, neg_idx = 0, 1
        for num in nums:
            if num > 0:
                result[pos_idx] = num
                pos_idx += 2
            else:
                result[neg_idx] = num
                neg_idx += 2

        return result