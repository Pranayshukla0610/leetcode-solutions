class Solution:
    def minSubArrayLen(self, target, nums):
        min_len = float('inf')
        left = 0
        total = 0
        n = len(nums)

        for right in range(n):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right-left + 1)
                total -= nums[left]
                left+= 1
        return min_len if min_len != float('inf') else 0

        