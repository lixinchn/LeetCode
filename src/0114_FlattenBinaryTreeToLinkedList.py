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
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack_left, stack_right = [], []
        self.do(root, stack_left, stack_right)

    def do(self, root, stack_left, stack_right):
        if not root:
            return

        if root.left:
            stack_left.append(root.left)
        if root.right:
            stack_right.insert(0, root.right)

        node = None
        if stack_left:
            node = stack_left[0]
            del stack_left[0]
            root.right = node
            root.left = None
        elif stack_right:
            node = stack_right[0]
            del stack_right[0]
            root.right = node
            root.left = None

        self.do(node, stack_left, stack_right)


if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([1,2,None,3,4,5])
    solution.flatten(head)
    print head
