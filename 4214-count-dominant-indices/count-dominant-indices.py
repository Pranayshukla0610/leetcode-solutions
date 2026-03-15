class Solution:
    def dominantIndices(self, nums):
        count = 0
        n = len(nums)

        for i in range(n - 1):   # last index not considered
            right = nums[i+1:]   # elements to the right
            avg = sum(right) / len(right)

            if nums[i] > avg:
                count += 1

        return count

        