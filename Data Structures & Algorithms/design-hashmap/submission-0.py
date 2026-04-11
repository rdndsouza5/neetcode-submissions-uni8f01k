class MyHashMap:

    def __init__(self):
        self.map =[]

    def put(self, key: int, value: int) -> None:
        for k, v in self.map:
            if k==key:
                self.map.remove((k,v))
        self.map.append((key,value))
        

    def get(self, key: int) -> int:
        for k, v in self.map:
            if k==key:
                return v
        return -1

        

    def remove(self, key: int) -> None:
        for k, v in self.map:
            if k==key:
                self.map.remove((k,v))
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)