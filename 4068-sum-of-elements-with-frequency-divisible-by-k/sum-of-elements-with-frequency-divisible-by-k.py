from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        total_sum = 0
        for num, count in freq.items():
            if count % k == 0:
                total_sum += num * count
        return total_sum


        