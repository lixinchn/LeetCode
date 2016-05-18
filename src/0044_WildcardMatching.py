class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        
        # dj[i][j] = dj[i - 1][j - 1] if p[i] == s[j] or p[i] == '?'
        #         = dj[i - 1][j] or dj[i][j - 1] if p[i] == '*'
        #         = False
        p = self.pre_treat_p(p)
        dj = []
        for i in range(len(s)):
            dj.append([])
            for j in range(len(p)):
                if p[j] == '?':
                    if i == 0 and j == 0:
                        dj[i].append(1)
                    elif i == 0 or j == 0:
                        dj[i].append(0)
                    else:
                        dj[i].append(dj[i - 1][j - 1])
                elif p[j] == '*':
                    if i == 0 and j == 0:
                        dj[i].append(1)
                    elif i == 0:
                        dj[i].append(dj[i][j - 1])
                    elif j == 0:
                        dj[i].append(dj[i - 1][j])
                    else:
                        dj[i].append(dj[i - 1][j] or dj[i][j - 1])
                else:
                    if s[i] == p[j]:
                        if i == 0 and j == 0:
                            dj[i].append(1)
                        elif i == 0 or j == 0:
                            dj[i].append(0)
                        else:
                            dj[i].append(dj[i - 1][j - 1])
                    else:
                        dj[i].append(0)

        if dj and dj[0]:
            return dj[-1][-1]
        if dj and not dj[0]:
            return False

        if not s:
            if not p or p == '*':
                return True
        return False



    def pre_treat_p(self, p):
        i = 0
        new_p = ''
        while i < len(p):
            if p[i] == '*':
                new_p += p[i]
                while i < len(p) and p[i] == '*':
                    i += 1
                continue
            new_p += p[i]
            i += 1
        return new_p


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
