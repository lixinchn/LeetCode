class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            try:
                stack.append(int(token))
                continue
            except:
                pass
            
            if token == '+' or token == '-' or token == '*' or token == '/':
                int2 = stack.pop()
                int1 = stack.pop()
                if token == '+':
                    res = int1 + int2
                elif token == '-':
                    res = int1 - int2
                elif token == '*':
                    res = int1 * int2
                else:
                    res = int(float(int1) / float(int2))
                stack.append(res)
        return stack[-1] if stack else None

if __name__ == "__main__":
    solution = Solution()
    print solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    print solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    print solution.evalRPN(['-1', '-4', '*']) == 4
    print solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

