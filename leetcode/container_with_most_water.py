"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""

class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            curr_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
            
            
if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    max_area = Solution().maxArea(height)
    print(max_area)
