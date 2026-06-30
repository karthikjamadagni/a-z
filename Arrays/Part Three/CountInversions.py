class Solution:

    def inversionCount(self, arr):
        return self.mergeSort(arr, 0, len(arr) - 1)

    def mergeSort(self, arr, l, r):
        count = 0
        
        if l < r:
            m = l + (r - l) // 2
            
            count += self.mergeSort(arr, l, m)
            count += self.mergeSort(arr, m + 1, r)
            count += self.merge(arr, l, m, r)
            
        return count
            
            
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        
        L = [0] * n1
        R = [0] * n2
        
        for i in range(n1):
            L[i] = arr[l + i]
            
        for i in range(n2):
            R[i] = arr[m + 1 + i]
            
        i = j = 0
        k = l
        count = 0
    
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                
                # Count inversions
                count += (n1 - i)
                
                j += 1
                
            k += 1
    
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            
        return count