class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self.backTrack([], 0)
        return self.res
    
    def backTrack(self, cur, noOpen):
        if len(cur)== 2* self.n:
            if noOpen == self.n:
                self.res.append(''.join(cur))
            return
        
        if noOpen < self.n:
            cur.append('(')
            self.backTrack(cur, noOpen+1)
            cur.pop()

        if len(cur)-noOpen < noOpen:
            cur.append(')')
            self.backTrack(cur, noOpen)
            cur.pop()
