class Solution(object):
    def c2n(self, c):
        if c == 'I':
            return 1
        elif c == 'V':
            return 5
        elif c == 'X':
            return 10
        elif c == 'L':
            return 50
        elif c == 'C':
            return 100
        elif c == 'D':
            return 500
        elif c == 'M':
            return 1000
        return 0
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, i = 0, 0
        while i < len(s):
            if i > 0 and self.c2n(s[i]) > self.c2n(s[i - 1]):
                result += (self.c2n(s[i]) - 2 * self.c2n(s[i - 1]))
            else:
                result += self.c2n(s[i])
            i += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    s = 'XXI'
    print solution.romanToInt(s)