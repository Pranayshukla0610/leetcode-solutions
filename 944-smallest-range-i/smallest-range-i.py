class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        min_value = min(nums)
        max_value = max(nums)

        result = max_value - min_value - 2 * k
        return max(0,result)