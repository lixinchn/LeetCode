import re
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def calc(a, b, o):
            return {'+':lambda x,y:x+y, '-':lambda x,y:x-y, '*':lambda x,y:x*y}[o](a, b)
        def dfs(nums, ops):
            if not ops:
                return [nums[0]]
            ans = []
            for x in range(len(ops)):
                left = dfs(nums[:x+1], ops[:x])
                right = dfs(nums[x+1:], ops[x+1:])
                for l in left:
                    for r in right:
                        ans.append(calc(l, r, ops[x]))
            return ans
        nums, ops = [], []
        input = re.split(r'(\D)', input)
        for x in input:
            if x.isdigit():
                nums.append(int(x))
            else:
                ops.append(x)
        return dfs(nums, ops)

solution = Solution()
print solution.diffWaysToCompute('2*3-4*5')
