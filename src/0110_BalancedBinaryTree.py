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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.do(root)

    def do(self, root):
        if not root:
            return True
        if not root.left:
            root.left_height = 0
        if not root.right:
            root.right_height = 0

        if root.left:
            if not self.do(root.left):
                return False
            root.left_height = max(root.left.left_height, root.left.right_height) + 1
        if root.right:
            if not self.do(root.right):
                return False
            root.right_height = max(root.right.left_height, root.right.right_height) + 1

        if root.left_height - root.right_height >= 2 or root.right_height - root.left_height >= 2:
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([3,9,20,None,None,5,5])
    print solution.isBalanced(head)
