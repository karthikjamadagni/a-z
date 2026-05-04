class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = cnt2 = 0
        ele1 = ele2 = None

        for num in nums:
            if num == ele1:
                cnt1 += 1
            elif num == ele2:
                cnt2 += 1
            elif cnt1 == 0:
                ele1 = num
                cnt1 = 1
            elif cnt2 == 0:
                ele2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # verification step (important!)
        result = []
        n = len(nums)

        if nums.count(ele1) > n // 3:
            result.append(ele1)
        if ele2 != ele1 and nums.count(ele2) > n // 3:
            result.append(ele2)

        return result