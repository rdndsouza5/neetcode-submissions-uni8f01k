class Node:
    def __init__(self):
        self.end = False
        self.hm = {}
    
class PrefixTree:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        prev = self.head
        for char in word:
            if char in prev.hm:
                prev = prev.hm[char]
            else:
                node = Node()
                prev.hm[char] = node
                prev = node
        prev.end = True



    def search(self, word: str) -> bool:
        prev = self.head
        for char in word:
            if char not in prev.hm:
                return False
            prev = prev.hm[char]
        if not prev.end:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        prev = self.head
        for char in prefix:
            if char not in prev.hm:
                return False
            prev = prev.hm[char]
        return True
        
        