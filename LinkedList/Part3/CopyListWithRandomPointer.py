# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Map original nodes to copied nodes
        listDict = {}

        temp = head

        # First pass: create all new nodes
        while temp:
            listDict[temp] = Node(temp.val)
            temp = temp.next

        temp = head

        # Second pass: assign next and random pointers
        while temp:
            if temp.next:
                listDict[temp].next = listDict[temp.next]
            else:
                listDict[temp].next = None

            if temp.random:
                listDict[temp].random = listDict[temp.random]
            else:
                listDict[temp].random = None

            temp = temp.next

        # Return copied head
        return listDict[head]