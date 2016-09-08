class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        s = s.strip()
        new_s = ''
        temp = ''
        for char in s:
            if char == ' ':
                if temp:
                    new_s += temp[::-1] + ' '
                    temp = ''
            else:
                temp += char
        if temp:
            new_s += temp[::-1]
        return new_s


if __name__ == "__main__":
    solution = Solution()
    print solution.reverseWords("the sky is blue")
    print solution.reverseWords('the     sky')
    print solution.reverseWords('   the       sky    ')
    print solution.reverseWords('the')
    print solution.reverseWords('   ')
    print solution.reverseWords('')
    print solution.reverseWords('    the')
    print solution.reverseWords('the   ')
    print solution.reverseWords('the')
    print solution.reverseWords('   a   b ') == 'b a'