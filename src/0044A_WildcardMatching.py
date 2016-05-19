class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i_s, i_p = 0, 0
        len_s, len_p = len(s), len(p)
        last_star, last_s = -1, -1
        while i_s < len_s:
            if i_p < len_p and (p[i_p] == s[i_s] or p[i_p] == '?'):
                i_p += 1
                i_s += 1
                continue
            if i_p < len_p and p[i_p] == '*':
                last_star = i_p
                i_p += 1
                last_s = i_s
                continue
            if last_star > -1:
                i_p = last_star + 1
                i_s = last_s + 1
                last_s += 1
                continue
            return False

        while i_p < len_p and p[i_p] == '*':
            i_p += 1

        return i_p >= len_p

if __name__ == "__main__":
    solution = Solution()
    print (solution.isMatch('a', '') == False)
    print (solution.isMatch('', 'a') == False)
    print (solution.isMatch('', '') == True)
    print (solution.isMatch('aa', 'a') == False)
    print (solution.isMatch('aa', 'aa') == True)
    print (solution.isMatch('aaa', 'aa') == False)
    print (solution.isMatch('aa', '*') == True)
    print (solution.isMatch('aa', 'a*') == True)
    print (solution.isMatch('ab', '?*') == True)
    print (solution.isMatch('aab', 'c*a*b') == False)
    print (solution.isMatch('*', '***') == True)
    print (solution.isMatch("aaabababaaabaababbbaaaabbbbbbabbbbabbbabbaabbababab", "*ab***ba**b*b*aaab*b") == True)
    print (solution.isMatch("aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", "a*******b") == False)
    print (solution.isMatch("abbbaaaaaaaabbbabaaabbabbbaabaabbbbaabaabbabaabbabbaabbbaabaabbabaabaabbbbaabbbaabaaababbbbabaaababbaaa", "ab**b*bb*ab**ab***b*abaa**b*a*aaa**bba*aa*a*abb*a*a") == True)
    print (solution.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a") == False)
