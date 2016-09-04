class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        l = []
        self.do(root, l)
        return l

    def do(self, root, l):
        if not root:
            return
        l.append(root.val)
        self.do(root.left, l)
        self.do(root.right, l)