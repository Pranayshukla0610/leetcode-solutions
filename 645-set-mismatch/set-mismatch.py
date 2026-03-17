from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicate = -1
        
        for x in nums:
            if x in seen:
                duplicate = x
            seen.add(x)
        
        # find missing
        for i in range(1, len(nums)+1):
            if i not in seen:
                missing = i
                break
        
        return [duplicate, missing]