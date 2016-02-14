class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            hLeft, hRight = height[left], height[right]
            min_height = min(hLeft, hRight)
            area = min_height * (right - left)
            if area > max_area:
                max_area = area

            if hLeft < hRight:
                left += 1
            elif hLeft > hRight:
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    height = (1, 2, 3)
    print solution.maxArea(height)