class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        len_s, len_t = len(s), len(t)
        if len_s != len_t:
            return False

        map_char_s = {}
        map_char_t = {}
        for i in range(len_s):
            c1 = s[i]
            c2 = t[i]
            if c1 in map_char_s or c2 in map_char_t:
                if c2 not in map_char_t or c1 not in map_char_s:
                    return False
                if map_char_s[c1] != map_char_t[c2]:
                    return False
                if t[map_char_t[c2]] != t[i]:
                    return False
            map_char_s[c1] = i
            map_char_t[c2] = i
        return True



        
if __name__ == "__main__":
    solution = Solution()
    # print solution.isIsomorphic('egg', 'add')
    # print solution.isIsomorphic('foo', 'bar')
    # print solution.isIsomorphic('paper', 'title')
    print solution.isIsomorphic('ab', 'aa')