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
        prev_nodes = []
        for val in arr:
            node = TreeNode(val)
            if not head:
                head = node
                this = node
                continue

            if left and right:
                this = prev_nodes.pop(0)
                left = False
                right = False
            if not left:
                this.left = node
                left = True
            elif not right:
                this.right = node
                right = True
            if node and node.val:
                prev_nodes.append(node)

        return head

class Solution(object):
    max_depth = 0
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        self.do(root, 1)
        return self.max_depth

    def do(self, root, depth):
        if root:
            if depth > self.max_depth:
                self.max_depth = depth

            if root.left:
                self.do(root.left, depth + 1)
            if root.right:
                self.do(root.right, depth + 1)



if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([3,9,20,None,None,15,7])
    print solution.maxDepth(head)

    print solution.maxDepth([])
