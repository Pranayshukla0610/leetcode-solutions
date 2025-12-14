class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        
        # Step 1: find current max candies
        max_candies = max(candies)
        
        # Step 2: result list
        result = []
        
        # Step 3: check each kid
        for c in candies:
            result.append(c + extraCandies >= max_candies)
        
        return result


        for c in candies:
            new_count = c + extraCandies
            res.append(new_count >= max_candies)
        return result
        