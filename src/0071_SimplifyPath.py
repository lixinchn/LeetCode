class Solution(object):
    ST_NORMAL = 0
    ST_DOT = 1
    ST_DOT_DOT = 2
    ST_SLASH = 3

    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_stack = []
        directory_name = ''
        current_st = self.ST_NORMAL

        for i in range(len(path)):
            char = path[i]
            if char == '/':
                if current_st == self.ST_NORMAL:
                    if directory_name:
                        path_stack.append(directory_name)
                        directory_name = ''
                    path_stack.append(char)
                    current_st = self.ST_SLASH
                    continue
                if current_st == self.ST_DOT:
                    directory_name = ''
                    current_st = self.ST_SLASH
                    continue
                if current_st == self.ST_DOT_DOT:
                    if len(path_stack) > 1:
                        path_stack.pop()
                        path_stack.pop()
                    directory_name = ''
                    current_st = self.ST_SLASH
                    continue
                if current_st == self.ST_SLASH:
                    continue
            if char == '.':
                if current_st == self.ST_NORMAL or current_st == self.ST_SLASH:
                    current_st = self.ST_DOT
                    continue
                if current_st == self.ST_DOT:
                    current_st = self.ST_DOT_DOT
                    continue
                if current_st == self.ST_DOT_DOT:
                    current_st = self.ST_NORMAL
                    directory_name += '...'
                    continue
                continue
            if current_st == self.ST_DOT:
                directory_name += '.'
            elif current_st == self.ST_DOT_DOT:
                directory_name += '..'
            directory_name += char
            current_st = self.ST_NORMAL

        if directory_name:
            path_stack.append(directory_name)
        if current_st == self.ST_DOT_DOT:
            if len(path_stack) > 1:
                path_stack.pop()
                path_stack.pop()
        if len(path_stack) > 1 and path_stack[-1] == '/':
            path_stack.pop()
        return ''.join(path_stack)



if __name__ == "__main__":
    solution = Solution()
    print solution.simplifyPath('/abc/...') == '/abc/...'

    print solution.simplifyPath('/..hidden') == '/..hidden'

    print solution.simplifyPath("/home/foo/.ssh/../.ssh2/authorized_keys/") == '/home/foo/.ssh2/authorized_keys'

    print solution.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///") == '/e/f/g'

    print solution.simplifyPath('///eHx/..') == '/'

