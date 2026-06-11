# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Leetcode hard. So skipping for the time being

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        temp = head
        kthNode = None

        def getKthNode(temp, k):
            k -= 1
            while temp and k > 0:
                k -= 1
                temp = temp.next

            return temp

        def reverseLinkedList(head):
            prev = None
            nxt = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        while temp:
            kthNode = getKthNode(temp, k)

            if not kthNode:
                if prev:
                    prev.next = temp
                    break

            nxt = kthNode.next
            kthNode.next = None
            reverseLinkedList(temp)

            if temp == head:
                head = kthNode
            else:
                prev.next = kthNode

            prev = temp
            temp = nxt

        return head

