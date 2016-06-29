class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        steps = [0, 1, 2]
        index = 3
        while index <= n:
            steps.append(steps[index - 1] + steps[index - 2])
            index += 1
        return steps[-1]


if __name__ == "__main__":
    solution = Solution()
    print solution.climbStairs(5)