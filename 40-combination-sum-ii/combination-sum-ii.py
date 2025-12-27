from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates easily

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])  # Found a valid combination
                return
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # If the number is too large, break (since sorted)
                if candidates[i] > remaining:
                    break
                # Recurse with next index (i+1) because each number can only be used once
                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

        backtrack(0, [], target)
        return res

# Example usage:
param_1 = [10,1,2,7,6,1,5]
param_2 = 8
ret = Solution().combinationSum2(param_1, param_2)
print(ret)

param_1 = [2,5,2,1,2]
param_2 = 5
ret = Solution().combinationSum2(param_1, param_2)
print(ret)


        