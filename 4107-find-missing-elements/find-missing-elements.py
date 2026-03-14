class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        missing_num = []
        start = min(nums)
        end = max(nums)

        for i in range(start,end+1):
            if i not in nums:
                missing_num.append(i)
        return missing_num



                


        