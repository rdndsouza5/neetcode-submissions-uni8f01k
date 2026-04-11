class TreeNode:
    def __init__(self, key=-1, val = -1, next=None):
        self.key= key
        self.value = val
        self.left = None
        self.right = None

class MyHashMap:

    def __init__(self):
        self.root = None
    
    def insert(self, root,key,value):
        if not root:
            return TreeNode(key,value)
        if key< root.key:
            root.left = self.insert(root.left,key,value)
        elif key> root.key:
            root.right = self.insert(root.right, key,value)
        else: 
            root.value=value
        return root
    
    def delete(self, root, key):
        if not root:
            return None
        if key< root.key:
            root.left = self.delete(root.left, key)
        elif key> root.key:
            root.right = self.delete(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                tmp= self.getMinValue(root.right)
                root.key= tmp.key
                root.value=tmp.value
                root.right = self.delete(root.right, tmp.key)
        return root

    def getMinValue(self, root):
        while root.left:
            root=root.left
        return root

    def put(self, key: int, value: int) -> None:
        self.root= self.insert(self.root, key,value)
        

    def get(self, key: int) -> int:
        cur =self.root
        while cur:
            if cur.key >key:
                cur= cur.left
            elif cur.key < key:
                cur= cur.right
            elif cur.key == key: 
                return cur.value
            else: 
                return -1

        return -1


    def remove(self, key: int) -> None:
        self.root= self.delete(self.root, key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)