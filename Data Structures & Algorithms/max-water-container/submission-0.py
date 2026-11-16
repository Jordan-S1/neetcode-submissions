class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mArea = 0
        l , r = 0, len(heights) - 1

        while(l < r):
            if heights[l] < heights[r]:
                area = heights[l] * (r - l)
                mArea = max(mArea, area)
                l += 1
            else:
                area = heights[r] * (r - l)
                mArea = max(mArea, area)
                r -= 1
        return mArea
            

