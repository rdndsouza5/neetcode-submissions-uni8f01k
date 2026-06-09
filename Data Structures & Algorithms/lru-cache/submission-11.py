class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        node.prev = prev
        prev.next = node
        node.next = nxt
        nxt.prev = node

    
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node =  self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            node.val = value
            self.insert(node)
            return
        if len(self.cache)== self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node
