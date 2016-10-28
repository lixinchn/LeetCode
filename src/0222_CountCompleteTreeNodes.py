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
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        height = 0
        temp = root
        while temp:
            height += 1
            temp = temp.left
        return self.do(root, height)


    def do(self, root, height):
        if height == 0 or not root:
            return 0
        if height == 1:
            return 1
        middle = self.find_middle(root, height)
        if middle:
            return 2 ** (height - 1) + self.do(root.right, height - 1)
        else:
            return 2 ** (height - 2) + self.do(root.left, height - 1)

    def find_middle(self, root, height):
        middle = root.left
        for i in range(height - 2):
            middle = middle.right
        return middle


if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([1,1,1,1,1])
    print solution.countNodes(head)
