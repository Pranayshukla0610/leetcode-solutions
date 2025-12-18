class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        present = set(nums)
        res = []
        for i in range(1, n+1):
            if i not in present:
                res.append(i)
        return res
        