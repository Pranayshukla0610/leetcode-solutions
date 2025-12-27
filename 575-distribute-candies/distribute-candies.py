from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        max_allowed = n // 2
        distinct_types = len(set(candyType))
        return min(distinct_types, max_allowed)

# Example usage:
candyType1 = [1,1,2,2,3,3]
candyType2 = [1,1,2,3]
candyType3 = [6,6,6,6]

sol = Solution()
print(sol.distributeCandies(candyType1))  # Output: 3
print(sol.distributeCandies(candyType2))  # Output: 2
print(sol.distributeCandies(candyType3))  # Output: 1

        