# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next

        k = k % n

        if k == 0:
            return head
        l = n - k
        count = 0
        temp = head
        while count < l-1 and temp:
            count += 1
            temp = temp.next

        newHead = temp.next
        temp.next = None

        newTail = newHead
        while newTail.next:
            newTail = newTail.next
        newTail.next = head

        head = newHead
        return head