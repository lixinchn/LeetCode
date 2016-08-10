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
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.do(root, sum)

    def do(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        if root.left:
            if self.do(root.left, sum - root.val):
                return True
        if root.right:
            if self.do(root.right, sum - root.val):
                return True
        return False



if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([-2, None, -3])
    print solution.hasPathSum(head, -5)
