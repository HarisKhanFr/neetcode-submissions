class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        highest = 0

        while l < r:
            temp = min(heights[l], heights[r]) * (r-l)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            if temp > highest:
                highest = temp
            
        return highest
        