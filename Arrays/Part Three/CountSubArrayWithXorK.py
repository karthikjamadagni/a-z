from typing import List

class Solution:
    def subarrayXor(self, arr: List[int], k: int) -> int:
        xor = 0
        freq = {0: 1}
        count = 0

        for num in arr:
            xor ^= num

            target = xor ^ k
            if target in freq:
                count += freq[target]

            freq[xor] = freq.get(xor, 0) + 1

        return count