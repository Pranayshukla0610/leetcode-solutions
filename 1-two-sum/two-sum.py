class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i

s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))


