class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def create(arr):
        head = None
        this = None
        left, right = False, False
        prev_node = None
        for val in arr:
            node = TreeNode(val)
            if not head:
                head = node
                this = node
                continue

            if left and right:
                this = prev_node
                left = False
                right = False
            if not left:
                this.left = node
                left = True
            elif not right:
                this.right = node
                right = True
            if node:
                prev_node = node

        return head

class Solution(object):
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.dfs(1, n)


    def dfs(self, start, end):
        if start > end: return [None]
        res = []
        for rootval in range(start, end + 1):
            LeftTree = self.dfs(start, rootval - 1)
            RightTree = self.dfs(rootval + 1, end)
            for i in LeftTree:
                for j in RightTree:
                    root = TreeNode(rootval)
                    root.left = i
                    root.right = j
                    res.append(root)
        return res

if __name__ == "__main__":
    solution = Solution()
    arr_ret = solution.generateTrees(3)
    print arr_ret
