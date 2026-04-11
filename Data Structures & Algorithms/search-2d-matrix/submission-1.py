class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLen = len(matrix)
        colLen = len(matrix[0])
        l= 0
        r = rowLen * colLen -1
        while l <= r:
            m = (l+ r )//2
            i = m//colLen
            j = m % colLen
            print(i,j)
            if matrix[i][j] ==  target:
                return True
            elif matrix[i][j] < target:
                l= m+1
            else:
                r= m-1
        return False