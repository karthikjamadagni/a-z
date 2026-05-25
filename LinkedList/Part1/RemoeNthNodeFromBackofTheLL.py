# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        req = length - n

        if req == 0:
            return head.next

        temp = head
        length = 0
        prev = None

        while length < req:
            prev = temp
            length += 1
            temp = temp.next

        prev.next = temp.next

        return head