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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.do(inorder, postorder, 0, len(inorder) - 1, 0, len(postorder) - 1)

    def do(self, inorder, postorder, inorder_left, inorder_right, postorder_left, postorder_right):
        if inorder_left > inorder_right:
            return None

        root_num = postorder[postorder_right]
        root = TreeNode(root_num)
        root_index_inorder = inorder.index(root_num)
        inorder_left_end = root_index_inorder - 1
        inorder_right_begin = root_index_inorder + 1
        postorder_left_end = (inorder_left_end - inorder_left) + postorder_left
        postorder_right_begin = postorder_left_end + 1
        root.left = self.do(inorder, postorder, inorder_left, inorder_left_end, postorder_left, postorder_left_end)
        root.right = self.do(inorder, postorder, inorder_right_begin, inorder_right, postorder_right_begin, postorder_right - 1)
        return root



if __name__ == "__main__":
    solution = Solution()
    head = solution.buildTree([4,2,5,1,6,3,7], [4,5,2,6,7,3,1])

