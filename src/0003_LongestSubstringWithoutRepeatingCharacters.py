class Solution(object):
    def get_char_index(self, s, char):
        for i in range(len(s)):
            if s[i] == char:
                return i
        return -1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, flag_start, longest = 0, 0, 0
        none_repeat_arr = []
        while True:
            if i >= len(s):
                break

            char = s[i]
            char_index = self.get_char_index(none_repeat_arr, char)
            none_repeat_arr.append(char)
            if char_index == -1:
                longest = len(none_repeat_arr) if len(none_repeat_arr) > longest else longest
            else:
                flag_start = char_index + 1
                none_repeat_arr = none_repeat_arr[flag_start:]
            i = i + 1
        return longest

if __name__ == "__main__":
    solution = Solution()
    print solution.lengthOfLongestSubstring('abcabcbb')
    print solution.lengthOfLongestSubstring('bbbbb')