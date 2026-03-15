class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min_time = float('inf')

        for s, t in tasks:
            finish = s + t
            min_time = min(min_time,finish)
        return min_time

        