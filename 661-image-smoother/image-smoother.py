from typing import List
import math

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        
        # Directions for neighbors including the cell itself
        directions = [(-1,-1), (-1,0), (-1,1),
                      (0,-1),  (0,0),  (0,1),
                      (1,-1),  (1,0),  (1,1)]
        
        for i in range(m):
            for j in range(n):
                total, count = 0, 0
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n:
                        total += img[x][y]
                        count += 1
                res[i][j] = total // count  # floor division
        return res

# Example usage:
img1 = [[1,1,1],[1,0,1],[1,1,1]]
img2 = [[100,200,100],[200,50,200],[100,200,100]]

sol = Solution()
print(sol.imageSmoother(img1))  
# Output: [[0,0,0],[0,0,0],[0,0,0]]

print(sol.imageSmoother(img2))  
# Output: [[137,141,137],[141,138,141],[137,141,137]]

        