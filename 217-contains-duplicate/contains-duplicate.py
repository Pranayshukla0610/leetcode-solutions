class Solution:
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:          # iterate over elements
            if num in seen:       # check if already exists
                return True
            seen.add(num)         # add number to set
        return False

        