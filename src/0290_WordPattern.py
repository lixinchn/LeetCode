class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        arr_str = str.split(' ')
        len_str = len(arr_str)
        if len_str != len(pattern):
            return False

        dict_word = {}
        dict_p = {}
        for i in range(len_str):
            word = arr_str[i]
            p = pattern[i]
            if word in dict_word:
                if p == dict_word[word]:
                    continue
                else:
                    return False
            if p in dict_p:
                if word != dict_p[p]:
                    return False
                else:
                    continue
            dict_word[word] = p
            dict_p[p] = word
        return True

solution = Solution()
print solution.wordPattern('abba', 'dog cat cat dog')
print solution.wordPattern('abba', 'dog cat cat fish')
print solution.wordPattern('aaaa', 'dog cat cat dog')
print solution.wordPattern('abba', 'dog dog dog dog')