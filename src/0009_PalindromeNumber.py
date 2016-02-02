class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        step = 1
        while x / step >= 10:
            step *= 10

        while x > 0:
            right = x % 10
            left = x / step
            if left != right:
                return False
            x = (x - left * step) / 10
            step /= 100
        return True

if __name__ == "__main__":
    solution = Solution()
    x = 121
    print solution.isPalindrome(x)

    x = 1221
    print solution.isPalindrome(x)

    x = 0
    print solution.isPalindrome(x)

    x = 1212
    print solution.isPalindrome(x)

    x = 123
    print solution.isPalindrome(x)

    x = 1001
    print solution.isPalindrome(x)
