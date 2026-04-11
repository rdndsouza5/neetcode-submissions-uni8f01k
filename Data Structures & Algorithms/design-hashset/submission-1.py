class MyHashSet:

    def __init__(self):
        self.items=[]

    def add(self, key: int) -> None:
        for i in self.items:
            if key == i:
                return
        self.items.append(key)
        

    def remove(self, key: int) -> None:
        for i in self.items:
            if i==key:
                self.items.remove(key)
        

    def contains(self, key: int) -> bool:
        for i in self.items:
            if i== key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)