class Solution:
    def maxCount(self, m: int, n: int, ops):
        # If no operations, entire matrix has the maximum value (0)
        if not ops:
            return m * n
        
        min_row = m
        min_col = n
        
        # Find intersection of all operations
        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)
        
        return min_row * min_col

        