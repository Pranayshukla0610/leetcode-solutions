from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        # Sort scores in descending order along with their original indices
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        
        # Prepare result array
        res = [""] * n
        
        # Assign ranks
        for rank, (s, idx) in enumerate(sorted_scores, start=1):
            if rank == 1:
                res[idx] = "Gold Medal"
            elif rank == 2:
                res[idx] = "Silver Medal"
            elif rank == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank)
        
        return res

# Example usage:
score1 = [5,4,3,2,1]
score2 = [10,3,8,9,4]

sol = Solution()
print(sol.findRelativeRanks(score1))  # ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
print(sol.findRelativeRanks(score2))  # ["Gold Medal","5","Bronze Medal","Silver Medal","4"]

        