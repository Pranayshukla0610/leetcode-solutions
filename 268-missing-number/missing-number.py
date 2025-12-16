class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)

        while l < r:
            mid = (l + r)//2
            if nums[mid] > mid:
                r = mid
            else:
                l = mid + 1
        return l
        