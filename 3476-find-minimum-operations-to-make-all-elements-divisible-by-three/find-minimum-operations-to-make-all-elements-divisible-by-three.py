class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min = 0
        for i in nums:
            if i % 3 != 0:
                min += 1
        return min
        