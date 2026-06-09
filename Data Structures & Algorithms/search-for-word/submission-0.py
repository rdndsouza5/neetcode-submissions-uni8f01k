class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    seen = set()
                    seen.add((i, j))
                    if self.checkWord(seen, board, word, i, j, 0):
                        return True
        return False

    def checkWord(self, usedLetters,board, word,i, j, charpos):
        if charpos>= len(word):
            return True
        if i>=len(board) or i<0:
            return False
        if j>=len(board[0]) or j< 0:
            return False
        if not  board[i][j]== word[charpos]:
            return False
        
        left = (i, j-1)
        right = (i, j+1)
        top = (i-1, j)
        bottom = (i+1, j)

        if left not in usedLetters:
            usedLetters.add(left)
            exists =self.checkWord(usedLetters,board, word, i, j-1, charpos+1) 
            if exists:
                return True
            usedLetters.remove(left)
        if right not in usedLetters:
            usedLetters.add(right)
            exists =self.checkWord(usedLetters, board,word, i, j+1, charpos+1) 
            if exists:
                return True
            usedLetters.remove(right)

        if top not in usedLetters:
            usedLetters.add(top)
            exists =self.checkWord(usedLetters,board, word, i-1, j, charpos+1) 
            if exists:
                return True
            usedLetters.remove(top)
        if bottom not in usedLetters:
            usedLetters.add(bottom)
            exists =self.checkWord(usedLetters,board, word, i+1, j, charpos+1) 
            if exists:
                return True
            usedLetters.remove(bottom)
        return False