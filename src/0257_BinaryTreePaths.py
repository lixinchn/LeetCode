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

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        self.ret_arr = []
        self.do(root, '')
        return self.ret_arr

    def do(self, root, prefix):
        if not root:
            if prefix:
                self.ret_arr.append(prefix)
            return

        if not prefix:
            prefix = '%s' % root.val
        else:
            prefix = '%s->%s' % (prefix, root.val)

        if root.left or root.right:
            if root.left:
                self.do(root.left, prefix)
            if root.right:
                self.do(root.right, prefix)
        else:
            self.do(None, prefix)


if __name__ == "__main__":
    solution = Solution()
    head1 = TreeNode.create([1,2,3,None,5])
    print solution.binaryTreePaths(head1)