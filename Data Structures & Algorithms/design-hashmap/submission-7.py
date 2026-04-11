class ListNode:
    def __init__(self, key=-1, val = -1, next=None):
        self.key= key
        self.value = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        cur = self.map[key%len(self.map)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)
        

    def get(self, key: int) -> int:
        cur = self.map[key%len(self.map)]
        while cur.next:
            if cur.next.key==key:
                return cur.next.value
            cur = cur.next
        return -1

    def hash(self, key: int) -> int:
        return key % len(self.map)


    def remove(self, key: int) -> None:
        cur = self.map[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)