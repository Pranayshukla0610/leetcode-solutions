class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_array = sorted(nums)

        for i in range(len(nums)):
            if sorted_array == nums:
                return True

            sorted_array = sorted_array[1:] + sorted_array[:1]

        return False