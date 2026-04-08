class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1 = 0
        p2 = len(heights) - 1
        max_area = 0 
        
        while p1 < p2:
            current_area = (p2 - p1) * min(heights[p1], heights[p2])
            
            if current_area > max_area:
                max_area = current_area
        
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
                
        return max_area