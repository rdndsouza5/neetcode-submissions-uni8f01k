class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie(dictionary).root
        hm = {len(s):0}
        def dfs(i):
            if i in hm:
                return hm[i]
            res = 1+ dfs(i+1)

            cur = trie
            j=i
            while j < len(s):
                if s[j] not in cur.children:
                    break
                cur = cur.children[s[j]]
                if cur.word:
                    res = min(res, dfs(j+1))
                j+=1
            
            hm[i]  = res
            
            return res
        return dfs(0)

class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = Node()
                cur = cur.children[c]
            cur.word = True
    