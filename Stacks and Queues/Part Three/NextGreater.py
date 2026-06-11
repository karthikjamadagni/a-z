class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = []
        hashmap = {}
        n = len(nums2)

        i = n - 1

        while i >= 0:
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if not stack:
                hashmap[nums2[i]] = -1
            else:
                hashmap[nums2[i]] = stack[-1]

            stack.append(nums2[i])

            i -= 1

        for i in range(len(nums1)):
            answer.append(hashmap[nums1[i]])

        return answer


            