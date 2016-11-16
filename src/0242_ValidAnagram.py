class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dict_s = {}
        for c in s:
            if dict_s.get(c, ''):
                dict_s[c] += 1
            else:
                dict_s[c] = 1

        for c in t:
            if not dict_s.get(c, ''):
                return False
            dict_s[c] -= 1
            if dict_s[c] == 0:
                del dict_s[c]
        return True

solution = Solution()
print solution.isAnagram('anagram', 'nagaram')
print solution.isAnagram('rat', 'car')