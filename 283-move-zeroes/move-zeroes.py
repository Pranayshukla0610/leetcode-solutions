class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[pos] = nums[r]
                pos += 1

        for i in range(pos,len(nums)):
            nums[i] = 0