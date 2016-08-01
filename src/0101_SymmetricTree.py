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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.do(root.left, root.right)


    def do(self, p, q):
        if p == None and q == None: return True
        if p and q and p.val == q.val:
            return self.do(p.right, q.left) and self.do(p.left, q.right)
        return False


if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([1,2,2, None,3,3])
    print solution.isSymmetric(head)
