class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        while True:
            if num >= 0 and num % 2 == 0:
                num /= 2
            else:
                break

        while True:
            if num >= 0 and num % 3 == 0:
                num /= 3
            else:
                break

        while True:
            if num >= 0 and num % 5 == 0:
                num /= 5
            else:
                break

        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        return False


solution = Solution()
print solution.isUgly(1)