class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hmap={}
        for  i, col in enumerate(board):
            for j, val in enumerate(col):
                if val ==".":
                    continue
                if (i+3,0) not in hmap:
                    hmap[i+3,0]=[]
                if (0,j+3) not in hmap:
                    hmap[0,j+3]=[]
                if (i//3,j//3) not in hmap:
                    hmap[i//3,j//3]=[]
                if val in hmap[i+3,0] or val in hmap[0,j+3] or val in hmap[i//3,j//3]:
                    return False
                hmap[i+3,0].append(val)
                hmap[0,j+3].append(val)
                hmap[i//3,j//3].append(val)
        return True