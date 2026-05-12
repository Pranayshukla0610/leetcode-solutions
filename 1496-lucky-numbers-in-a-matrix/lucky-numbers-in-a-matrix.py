class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        for i in range(len(matrix)):
            row_min = min(matrix[i])
            max_col = float('-inf')
            col_index = matrix[i].index(row_min)
            max_col = float('-inf')
            for j in range(rows):
                max_col = max(max_col,matrix[j][col_index])

            if row_min == max_col:
                result.append(row_min)

        return result
        