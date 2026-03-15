class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        min_dist = float('inf')
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        dist = abs(i - j) + abs(j - k) + abs(k - i)
                        min_dist = min(min_dist,dist)
        if min_dist == float('inf'):
            return -1
        else:
            return min_dist
        