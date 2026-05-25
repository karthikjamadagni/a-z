class Solution:
    def addOne(self, head):

        def reverse(head):
            prev = None
            curr = head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        head = reverse(head)

        temp = head

        carry = 1   # initially add one

        while temp and carry:

            val = temp.data + carry

            if val == 10:
                carry = 1
                temp.data = 0

            else:
                temp.data = val
                carry = 0

            temp = temp.next

        head = reverse(head)

        if carry == 1:
            newHead = Node(1)
            newHead.next = head
            head = newHead

        return head