class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        positiveDiagonal = set() 
        negativeDiagonal = set()

        board= [["."]*n for i in range(n)]

        res = []

        def backTrack(r):
            if r== n:
                copy=["".join(r) for r in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or r+c in positiveDiagonal or r-c in negativeDiagonal:
                    continue
                
                col.add(c)
                positiveDiagonal.add(r+c)
                negativeDiagonal.add(r-c)

                board[r][c]="Q"
                backTrack(r+1)

                col.remove(c)
                positiveDiagonal.remove(r+c)
                negativeDiagonal.remove(r-c)
                board[r][c]="."
        backTrack(0)
        return res