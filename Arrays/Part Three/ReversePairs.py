class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        count = 0
        
        if l < r:
            m = l + (r - l) // 2
            
            count += self.mergeSort(nums, l, m)
            count += self.mergeSort(nums, m + 1, r)
            
            count += self.merge(nums, l, m, r)
            
        return count


    def merge(self, nums, l, m, r):
        count = 0
        
        # Count reverse pairs
        j = m + 1
        
        for i in range(l, m + 1):
            while j <= r and nums[i] > 2 * nums[j]:
                j += 1
            
            count += (j - (m + 1))
        
        
        # Normal merge (same as your merge sort)
        n1 = m - l + 1
        n2 = r - m
        
        L = [0] * n1
        R = [0] * n2
        
        for i in range(n1):
            L[i] = nums[l + i]
            
        for i in range(n2):
            R[i] = nums[m + 1 + i]
            
        i = j = 0
        k = l
        
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
                
            k += 1
            
        while i < n1:
            nums[k] = L[i]
            i += 1
            k += 1
            
        while j < n2:
            nums[k] = R[j]
            j += 1
            k += 1
            
        return count