class Solution:
    def maxArea(self,height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            width = r - l
            curr_height = min(height[l], height[r])
            max_area = max(max_area, width * curr_height)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area