# have to do

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, node):
        prevNode, nxtNode = node.prev, node.nxt
        prevNode.nxt = nxtNode
        nxtNode.prev = prevNode

    def insert(self, node):
        nxtNode, prevNode = self.right, self.right.prev
        prevNode.nxt = node
        node.prev = prevNode
        node.nxt = nxtNode
        nxtNode.prev = node

        

    def get(self, key: int) -> int:
        if key in self.cache:
            tbr = self.cache[key].val
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return tbr
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)