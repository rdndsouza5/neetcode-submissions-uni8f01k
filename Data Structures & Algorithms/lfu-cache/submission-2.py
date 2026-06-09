class Node:
    def __init__(self, key, val):
        self.key = key
        self.freq = 1
        self.val = val
        self.prev = self.next = None

class LinkedList:
    def __init__(self):
        self.left, self.right = Node(0, 0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return  self.size

    def pushRight(self,node):
        prev, nxt = self.right.prev, self.right
        
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt
        self.size+=1


    def pop(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        self.size -= 1
        node.prev = node.next = None
        return
    
    def popleft(self):
        node = self.left.next
        self.pop( node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.listMap= defaultdict(LinkedList)
        self.lfuCount = 0

    def counter(self, node):
        freq = node.freq
        self.listMap[freq].pop(node)
        if self.lfuCount== freq and self.listMap[freq].length()==0:
            self.lfuCount+=1
        node.freq+=1
        self.listMap[node.freq].pushRight(node)
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.counter(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap==0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.counter(node)
            return
        if len(self.cache)==self.cap:
            node = self.listMap[self.lfuCount].popleft()
            del self.cache[node.key]
        
        node = Node(key, value)
        self.lfuCount = 1
        self.cache[key] = node
        self.listMap[1].pushRight(node)
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)