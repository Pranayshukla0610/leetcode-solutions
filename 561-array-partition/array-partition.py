from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))

# Example usage:
nums1 = [1,4,3,2]
nums2 = [6,2,6,5,1,2]

sol = Solution()
print(sol.arrayPairSum(nums1))  # Output: 4
print(sol.arrayPairSum(nums2))  # Output: 9

        