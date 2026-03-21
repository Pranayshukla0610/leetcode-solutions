from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()  # sort every time
            
            x = stones.pop()     # largest
            y = stones.pop()     # second largest
            
            if x != y:
                stones.append(x - y)
        
        return stones[0] if stones else 0
        