class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        left_parentheses_num = 0
        left_parentheses_stack = []
        parentheses_flag = []
        for i in range(len(s)):
            if s[i] == '(':
                left_parentheses_num += 1
                left_parentheses_stack.append(i)
                parentheses_flag.append(0)
                continue
            if left_parentheses_num > 0:
                left_index = left_parentheses_stack.pop()
                parentheses_flag.append(1)
                parentheses_flag[left_index] = 1
                left_parentheses_num -= 1
                continue
            parentheses_flag.append(0)

        longest_num = 0
        longest_num_temp = 0
        for i in range(len(parentheses_flag)):
            if parentheses_flag[i] == 0:
                longest_num = max(longest_num, longest_num_temp)
                longest_num_temp = 0
                continue
            longest_num_temp += 1
        longest_num = max(longest_num, longest_num_temp)
        return longest_num
            
        
if __name__ == "__main__":
    solution = Solution()
    strs = '(()'
    print solution.longestValidParentheses(strs)
