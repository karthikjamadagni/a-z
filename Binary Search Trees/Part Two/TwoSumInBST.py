class Solution:

    def initialize_next_stack(self, root):
        self.next_stack = []
        while root:
            self.next_stack.append(root)
            root = root.left

    def initialize_previous_stack(self, root):
        self.previous_stack = []
        while root:
            self.previous_stack.append(root)
            root = root.right

    def next_element(self):
        node = self.next_stack.pop()
        val = node.val

        node = node.right
        while node:
            self.next_stack.append(node)
            node = node.left

        return val

    def previous_element(self):
        node = self.previous_stack.pop()
        val = node.val

        node = node.left
        while node:
            self.previous_stack.append(node)
            node = node.right

        return val

    def findTarget(self, root, k):
        if not root:
            return False

        self.initialize_next_stack(root)
        self.initialize_previous_stack(root)

        left = self.next_element()
        right = self.previous_element()

        while left < right:
            curr_sum = left + right

            if curr_sum == k:
                return True
            elif curr_sum < k:
                left = self.next_element()
            else:
                right = self.previous_element()

        return False