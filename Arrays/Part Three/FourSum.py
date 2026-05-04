class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        output = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                left = j+1
                right = len(nums)-1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        output.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[left+1] == nums[left]  :
                            left += 1

                        while left < right and nums[right] == nums[right-1]  :
                            right -= 1

                        left += 1
                        right -= 1

                    elif current_sum < target:
                        left += 1

                    else:
                        right -= 1


        return output




            