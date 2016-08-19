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
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        arr_max_root = [-1 * (1 << 31)]
        max_val = self.do(root, arr_max_root)
        return max(max_val, arr_max_root[0])

    def do(self, root, arr_max_root):
        if not root:
            return -1 * (1 << 31)

        left_val = self.do(root.left, arr_max_root)
        right_val = self.do(root.right, arr_max_root)
        max_val = root.val
        if left_val > 0:
            max_val += left_val
        if right_val > 0:
            max_val += right_val
        arr_max_root[0] = max(arr_max_root[0], max_val)
        return max(root.val, max(root.val + left_val, root.val + right_val))



if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([3,1,2])
    print solution.maxPathSum(head)
    head = TreeNode.create([-2,6,None,0,-6])
    print solution.maxPathSum(head)
    head = TreeNode.create([-3])
    print solution.maxPathSum(head)
    head = TreeNode.create([1,-2,-3,1,3,-2,None,-1])
    print solution.maxPathSum(head)
