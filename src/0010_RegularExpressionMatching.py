class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s += '\0'
        p += '\0'
        p = self.pre_handle_p(p)
        print p
        return self.isMatchWithIndex(s, p, 0, 0)

    def pre_handle_p(self, p):
        previous_star_char = ''
        ret_p = ''
        index = 0
        while True:
            if p[index] == '\0':
                ret_p += '\0'
                break

            if p[index + 1] == '*':
                if p[index] == previous_star_char:
                    index += 2
                    continue
                previous_star_char = p[index]
                ret_p += p[index] + p[index + 1]
                index += 2
                continue

            previous_star_char = ''
            ret_p += p[index]
            index += 1
        return ret_p


    def isMatchWithIndex(self, s, p, index_s, index_p):
        if p[index_p] == '\0':
            return s[index_s] == '\0'

        if p[index_p + 1] != '*':
            return ((p[index_p] == s[index_s]) or (p[index_p] == '.' and s[index_s] != '\0')) and self.isMatchWithIndex(s, p, index_s + 1, index_p + 1)

        # p[index_p + 1] == '*'

        while p[index_p] == s[index_s] or (p[index_p] == '.' and s[index_s] != '\0'):
            if self.isMatchWithIndex(s, p, index_s, index_p + 2):
                return True
            index_s += 1
        return self.isMatchWithIndex(s, p, index_s, index_p + 2)

if __name__ == "__main__":
    solution = Solution()
    s, p = 'aa', 'aa'
    print solution.isMatch(s, p)

    s, p = 'aa', 'a'
    print solution.isMatch(s, p)

    s, p = 'aaa', 'aa'
    print solution.isMatch(s, p)

    s, p = 'aa', 'a*'
    print solution.isMatch(s, p)

    s, p = 'aa', '.*'
    print solution.isMatch(s, p)

    s, p = 'ab', '.*'
    print solution.isMatch(s, p)

    s, p = 'aab', 'c*a*b'
    print solution.isMatch(s, p)

    s, p = 'aaa', 'aaaa'
    print solution.isMatch(s, p)

    s, p = 'aaa', 'a*a'
    print solution.isMatch(s, p)

    s, p = 'aaa', 'ab*a*c*a'
    print solution.isMatch(s, p)

    s, p = "aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"
    print solution.isMatch(s, p)

    s, p = "bbbaccbbbaababbac", ".b*b*.*...*.*c*."
    print solution.isMatch(s, p)

