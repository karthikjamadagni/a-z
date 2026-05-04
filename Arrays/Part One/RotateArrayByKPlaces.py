class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse_array(x, y):

            while x < y:
                nums[x], nums[y] = nums[y], nums[x]
                x += 1
                y -= 1


        n = len(nums)
        k = k % n
        if n == 1:
            return      
        reverse_array(0, n-1)
        reverse_array(0, k-1)
        reverse_array(k, n-1)
