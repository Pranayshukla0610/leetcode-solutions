class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        longest = 0
        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                if length > longest:
                    longest = length
        return longest
        