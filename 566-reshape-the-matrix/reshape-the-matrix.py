class Solution:
    def matrixReshape(self, mat, r, c):
        m, n = len(mat), len(mat[0])
        
        # If reshape is not possible, return original matrix
        if m * n != r * c:
            return mat
        
        # Flatten the matrix
        flat = []
        for row in mat:
            flat.extend(row)
        
        # Build the reshaped matrix
        reshaped = []
        idx = 0
        for _ in range(r):
            reshaped.append(flat[idx:idx + c])
            idx += c
        
        return reshaped

        