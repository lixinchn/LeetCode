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
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.nums = 0
        self.do(root, '')
        return self.nums

    def do(self, root, str_num):
        if not root.left and not root.right:
            str_num += str(root.val)
            self.nums += int(str_num) if str_num else 0
            return

        if root.left:
            self.do(root.left, str_num + str(root.val))
        if root.right:
            self.do(root.right, str_num + str(root.val))


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode.create([1,1,1,2])
    print solution.sumNumbers(root)