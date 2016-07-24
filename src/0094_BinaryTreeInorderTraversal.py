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
        prev_node = None
        for val in arr:
            node = TreeNode(val)
            if not head:
                head = node
                this = node
                continue

            if left and right:
                this = prev_node
                left = False
                right = False
            if not left:
                this.left = node
                left = True
            elif not right:
                this.right = node
                right = True
            if node:
                prev_node = node

        return head


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        arr_ret = []
        self.do(root, arr_ret)
        return arr_ret

    def do(self, root, arr_ret):
        if root.left:
            self.do(root.left, arr_ret)
        if root.val:
            arr_ret.append(root.val)
        if root.right:
            self.do(root.right, arr_ret)

if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([1,None,2,3])
    print solution.inorderTraversal(head)
    
        