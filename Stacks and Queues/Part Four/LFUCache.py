# have to do --> VEry very hard

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.nxt = None


class DLL:
    # Doubly Linked List for each frequency
    def __init__(self):
        self.left = Node(0, 0)   # dummy head
        self.right = Node(0, 0)  # dummy tail
        self.left.nxt = self.right
        self.right.prev = self.left
        self.size = 0

    def insert(self, node):
        # insert at right (most recently used in this freq)
        prevNode = self.right.prev
        prevNode.nxt = node
        node.prev = prevNode
        node.nxt = self.right
        self.right.prev = node
        self.size += 1

    def remove(self, node):
        prevNode, nxtNode = node.prev, node.nxt
        prevNode.nxt = nxtNode
        nxtNode.prev = prevNode
        self.size -= 1

    def popLeft(self):
        # remove least recently used in this freq
        if self.size > 0:
            node = self.left.nxt
            self.remove(node)
            return node
        return None


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.keyMap = {}
        self.freqMap = {}
        self.minFreq = 0

    def updateFreq(self, node):
        freq = node.freq
        self.freqMap[freq].remove(node)

        # update minFreq if needed
        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DLL()

        self.freqMap[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self.updateFreq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.updateFreq(node)
        else:
            if len(self.keyMap) == self.cap:
                # Evict LFU
                lfuList = self.freqMap[self.minFreq]
                nodeToRemove = lfuList.popLeft()
                del self.keyMap[nodeToRemove.key]

            newNode = Node(key, value)
            self.keyMap[key] = newNode
            self.minFreq = 1

            if 1 not in self.freqMap:
                self.freqMap[1] = DLL()

            self.freqMap[1].insert(newNode)