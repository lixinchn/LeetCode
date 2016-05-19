class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = self.remove_repeated_star(p)
        return self.do(s, p, 0, 0, len(s), len(p))

    def remove_repeated_star(self, p):
        new_p = ''
        previous_star_char = ''
        i, len_p = 0, len(p)
        while i < len_p:
            if i + 1 < len_p and p[i + 1] == '*' and p[i] == previous_star_char:
                i += 2
                continue
            if p[i] == '*':
                if i > 0:
                    previous_star_char = new_p[-1]
                new_p += p[i]
                i += 1
                while i < len_p and p[i] == '*':
                    i += 1
                continue
            new_p += p[i]
            i += 1
            previous_star_char = ''
        return new_p

    def do(self, s, p, i_s, i_p, len_s, len_p):
        if i_p >= len_p:
            return i_s >= len_s

        if i_p + 1 < len_p and p[i_p + 1] == '*':
            while i_s < len_s and (s[i_s] == p[i_p] or p[i_p] == '.'):
                if self.do(s, p, i_s, i_p + 2, len_s, len_p):
                    return True
                i_s += 1
            return self.do(s, p, i_s, i_p + 2, len_s, len_p)
        else:
            return (i_s < len_s and (p[i_p] == '.' or p[i_p] == s[i_s])) and self.do(s, p, i_s + 1, i_p + 1, len_s, len_p)


if __name__ == "__main__":
    solution = Solution()
    s, p = 'aa', 'aa'
    print solution.isMatch(s, p) == True

    s, p = 'aa', 'a'
    print solution.isMatch(s, p) == False

    s, p = 'aaa', 'aa'
    print solution.isMatch(s, p) == False

    s, p = 'aa', 'a*'
    print solution.isMatch(s, p) == True

    s, p = 'aa', '.*'
    print solution.isMatch(s, p) == True

    s, p = 'ab', '.*'
    print solution.isMatch(s, p) == True

    s, p = 'aab', 'c*a*b'
    print solution.isMatch(s, p) == True

    s, p = 'aaa', 'aaaa'
    print solution.isMatch(s, p) == False

    s, p = 'aaa', 'a*a'
    print solution.isMatch(s, p) == True

    s, p = 'aaa', 'ab*a*c*a'
    print solution.isMatch(s, p) == True

    s, p = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
    print solution.isMatch(s, p) == False

    s, p = "bbbaccbbbaababbac", ".b*b*.*...*.*c*."
    print solution.isMatch(s, p) == True

    s, p = 'a', 'ab*'
    print solution.isMatch(s, p) == True

    s, p = 'a', '.*..a*'
    print solution.isMatch(s, p) == False

