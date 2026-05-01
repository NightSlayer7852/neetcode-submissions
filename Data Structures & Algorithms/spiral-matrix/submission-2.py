class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        i, j = 0, 0
        
        # Total elements to visit
        total = m * n
        res.append(matrix[i][j])
        matrix[i][j] = -101 # Mark visited
        
        while len(res) < total:
            # 1. Move Right as far as possible
            while j + 1 < n and matrix[i][j + 1] != -101:
                j += 1
                res.append(matrix[i][j])
                matrix[i][j] = -101
            
            # 2. Move Down as far as possible
            while i + 1 < m and matrix[i + 1][j] != -101:
                i += 1
                res.append(matrix[i][j])
                matrix[i][j] = -101
                
            # 3. Move Left as far as possible
            while j - 1 >= 0 and matrix[i][j - 1] != -101:
                j -= 1
                res.append(matrix[i][j])
                matrix[i][j] = -101
                
            # 4. Move Up as far as possible
            while i - 1 >= 0 and matrix[i - 1][j] != -101:
                i -= 1
                res.append(matrix[i][j])
                matrix[i][j] = -101
                
        return res
