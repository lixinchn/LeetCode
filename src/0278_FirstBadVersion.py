def isBadVersion(n):
    if n >= 3:
        return True
    return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        first_bad = 0
        while left <= right:
            middle = (left + right) / 2
            if isBadVersion(middle):
                if not first_bad or first_bad > middle:
                    first_bad = middle
                right = middle - 1
            else:
                left = middle + 1
        return first_bad

solution = Solution()
print solution.firstBadVersion(10)