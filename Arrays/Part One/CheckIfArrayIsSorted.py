class Solution:
    def check(self, arr: List[int]) -> bool:
        count_ascending_order_broken = 0
        n = len(arr)
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                count_ascending_order_broken += 1

        if arr[n-1] > arr[0]:
            count_ascending_order_broken += 1

        if count_ascending_order_broken > 1:
            return False

        else:
            return True