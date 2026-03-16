class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        unique_nums = list(set(nums))
        unique_nums.sort(reverse=True)
        return unique_nums[:k]
        