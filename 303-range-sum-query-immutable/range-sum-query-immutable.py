class NumArray:
    def __init__(self, nums):
        # Precompute prefix sums
        self.prefix_sums = [0]  # prefix_sums[i] = sum of nums[0] to nums[i-1]
        for num in nums:
            self.prefix_sums.append(self.prefix_sums[-1] + num)
    
    def sumRange(self, left, right):
        # Sum from left to right = prefix_sums[right + 1] - prefix_sums[left]
        return self.prefix_sums[right + 1] - self.prefix_sums[left]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)