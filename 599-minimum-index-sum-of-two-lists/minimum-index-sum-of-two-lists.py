from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {s: i for i, s in enumerate(list1)}
        
        min_sum = float('inf')
        result = []
        
        for j, s in enumerate(list2):
            if s in index_map:
                current_sum = index_map[s] + j
                
                if current_sum < min_sum:
                    min_sum = current_sum
                    result = [s]
                elif current_sum == min_sum:
                    result.append(s)
        
        return result

        