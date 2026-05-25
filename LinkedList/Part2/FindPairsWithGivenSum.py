from typing import Optional, List

class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        
        if not head:
            return []

        low = head
        high = head

        # Move high to last node
        while high.next:
            high = high.next

        res = []

        while low and high and low != high and high.next != low:

            total = low.data + high.data

            if total == target:
                res.append([low.data, high.data])
                low = low.next
                high = high.prev

            elif total < target:
                low = low.next

            else:
                high = high.prev

        return res