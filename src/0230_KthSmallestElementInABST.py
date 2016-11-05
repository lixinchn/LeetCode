class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = 0
        return self.do(root, k)

    def do(self, root, k):
        if root.left:
            num = self.do(root.left, k)
            if num != None:
                return num

        self.count += 1
        if self.count == k:
            return root.val

        if root.right:
            num = self.do(root.right, k)
            if num != None:
                return num