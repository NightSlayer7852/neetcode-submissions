class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowl, rowr = 0, len(matrix) - 1

        while( rowl <= rowr):
            rowm = (rowl + rowr) // 2
            if target > matrix[rowm][-1]:
                rowl = rowm + 1
            elif target < matrix[rowm][0]:
                rowr = rowm - 1
            else:
                break
        
        if not rowl<=rowr:
            return False

        row = (rowl + rowr) // 2
        l, r = 0, len(matrix[0]) - 1
        while(l <= r):
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        
        return False