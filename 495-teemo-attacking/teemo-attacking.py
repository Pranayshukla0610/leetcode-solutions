class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        
        totalPoisonedTime = 0
        
        for i in range(len(timeSeries) - 1):
            # Add the smaller of duration or the gap to next attack
            totalPoisonedTime += min(duration, timeSeries[i+1] - timeSeries[i])
        
        # Add duration for the last attack
        totalPoisonedTime += duration
        
        return totalPoisonedTime

        