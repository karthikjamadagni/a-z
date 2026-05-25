# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def findMiddle(head):
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow    

        def mergeSort(head):
            if not head or not head.next:
                return head
            middle = findMiddle(head)
            right = middle.next
            middle.next = None
            left = head
            left = mergeSort(head)
            right = mergeSort(right)

            return merge(left, right)

        def merge(left, right):
            dummyNode = ListNode(-1)
            temp = dummyNode

            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                    temp = temp.next

                else:
                    temp.next = right
                    right = right.next
                    temp = temp.next

            if left:
                temp.next = left

            else:
                temp.next = right

            return dummyNode.next

        return mergeSort(head)

