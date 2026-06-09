class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie(words).root
        row = len(board)
        col = len(board[0])
        res = []
        string = []
        seen = set() 
        def dfs(r, c, cur):
            if r<0 or c<0 or r>=row or c>=col or board[r][c] not in cur.children or (r,c) in seen:
                return
            seen.add((r,c))
            cur = cur.children[board[r][c]]
            string.append(board[r][c])
            if cur.word:
                res.append(''.join(string))
            dfs(r+1,c, cur)
            dfs(r-1, c, cur)
            dfs(r, c+1, cur)
            dfs(r, c-1, cur)
            seen.remove((r,c))
            string.pop()

        for r in range(row):
            for c in range(col):
                if board[r][c] in root.children:
                    dfs(r,c , root)


        
        res = set(res)
        return list(res)
    
                    
                    

class Trie:
    def __init__(self, words):
        self.root = Node()
        for word in words:
            cur = self.root
            for c in word:
                if c not in cur.children:
                    cur.children[c]= Node()
                cur = cur.children[c]
            cur.word = True
                
class Node:
    def __init__(self):
        self.word = False
        self.children = {}