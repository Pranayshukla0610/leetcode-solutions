class Solution:
    def getRow(self, rowIndex: int):
        row = [1]  # The first element is always 1
        for i in range(1, rowIndex + 1):
            # Compute next element using the previous element
            row.append(row[-1] * (rowIndex - i + 1) // i)
        return row
        