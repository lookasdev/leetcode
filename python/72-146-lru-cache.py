# from typing import Optional

class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Optional["Node"] = None
        self.next: Optional["Node"] = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # key -> Node

        # left = LRU (least recent), right = MRU (most recent)
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from its current position in the doubly linked list
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # insert node at the right (most recent) position
    def insert(self, node: Node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)  # move to MRU
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        # evict least recently used if over capacity
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            # If the Node only had the value, we wouldn’t know which key to delete from self.cache.
            # The key in self.cache (dict) is the same as node.key stored inside the node.
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)