class Solution:
    def removeElement(self, nums, val):
        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]   # place the kept value at index l
                l += 1             # then move l to next free slot
        return l


        