class Solution:
    def minimumSumSubarray(self, nums, l: int, r: int):
        min_sum = float('inf')
        n = len(nums)

        for left in range(n):
            curr_sum = 0
            for right in range(left,n):
                curr_sum += nums[right]
                length = right - left + 1
                if l <= length <= r and curr_sum > 0:
                    min_sum = min(min_sum,curr_sum)
        return min_sum if min_sum != float('inf') else -1
        