class Solution:
    def findUnion(self, a, b):
        i, j = 0, 0
        n, m = len(a), len(b)
        union = []
    
        while i < n and j < m:
            # Skip duplicates in a
            if i > 0 and a[i] == a[i - 1]:
                i += 1
                continue
    
            # Skip duplicates in b
            if j > 0 and b[j] == b[j - 1]:
                j += 1
                continue
    
            if a[i] < b[j]:
                union.append(a[i])
                i += 1
            elif a[i] > b[j]:
                union.append(b[j])
                j += 1
            else:
                union.append(a[i])
                i += 1
                j += 1
    
        # Remaining elements in a
        while i < n:
            if i == 0 or a[i] != a[i - 1]:
                union.append(a[i])
            i += 1
    
        # Remaining elements in b
        while j < m:
            if j == 0 or b[j] != b[j - 1]:
                union.append(b[j])
            j += 1
    
        return union