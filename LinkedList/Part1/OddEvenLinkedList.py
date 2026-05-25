# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        oddHead = None
        oddTail = None
        evenHead = None
        evenTail = None
        count = 0

        temp = head

        while temp:
            nxt = temp.next
            temp.next = None   # break old links
            if count % 2 == 0:
                if not oddHead:
                    oddHead = oddTail = temp

                else:
                    oddTail.next = temp
                    oddTail = oddTail.next

            else:
                if not evenHead:
                    evenHead = evenTail = temp
                else:
                    evenTail.next = temp
                    evenTail = evenTail.next

            count += 1
            temp = nxt

        oddTail.next = evenHead
        return oddHead