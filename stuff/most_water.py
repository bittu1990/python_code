"""Given n non-negative integers a1, a2, ..., an , where each represents a point at 
coordinate (i, ai). n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a 
container, such that the container contains the most water."""

height  = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    maxArea = 0
    left = 0
    right = len(height)-1
    while left!= right:
        width=right-left
        if height[left] <= height[right]:
            area = width*height[left]
            left += 1
        else:
            area = width*height[right]
            right -= 1
        if area>maxArea:
            maxArea = area
    return maxArea

print(maxArea(height))
