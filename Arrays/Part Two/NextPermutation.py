class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        bp = -1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                bp = i
                break

        if bp == -1:
            nums.reverse()
            return

        
        for i in range(len(nums)-1, bp, -1):
            if nums[i] > nums[bp]:
                temp = nums[i]
                nums[i] = nums[bp]
                nums[bp] = temp
                break

        self.reverse(bp+1, nums)

    def reverse(self, index: int, nums: List[int]) -> None:
        i = index
        j = len(nums)-1

        while i<j:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

            i+=1
            j-=1
        