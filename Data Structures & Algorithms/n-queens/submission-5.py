class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [['.']*n for i in range(n)]

        cols = set()
        posDiag = set()
        negDiag = set()

        def backTrack(r):
            if r == n:
                copy = [''.join(b) for b in board]
                res.append(copy)
                return

            for c in range(n):
                if (c in cols or (r+c) in posDiag or (r-c) in negDiag):
                    continue
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backTrack(r+1)
                cols.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] ="."
        backTrack(0)
        return res