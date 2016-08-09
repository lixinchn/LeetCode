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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.do(root)
        return root.depth if root else 0

    def do(self, root):
        if not root:
            return

        root.depth = 0
        if not root.left and not root.right:
            root.depth = 1
            return

        if root.left:
            self.do(root.left)
            if not root.depth or root.depth > root.left.depth + 1:
                root.depth = root.left.depth + 1
        if root.right:
            self.do(root.right)
            if not root.depth or root.depth > root.right.depth + 1:
                root.depth = root.right.depth + 1 



if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([3,1,2])
    print solution.minDepth(head)
