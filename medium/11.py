class Solution(object):
    def maxArea(self, height):
        max_water = 0
        i = 0
        j = len(height) - 1
        while i<j:
            current = min(height[i], height[j])*(j-i)
            max_water = max(current, max_water)

            if height[i]>height[j]:
                j=j-1
            else:
                i=i+1
                
        return max_water
        
        