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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ancestors_p = []
        ancestors_q = []
        temp_p, temp_q = root, root
        while True:
            if not temp_p:
                ancestors_p = []
                break
            
            ancestors_p.append(temp_p)
            if temp_p.val == p.val:
                break
            elif temp_p.val < p.val:
                temp_p = temp_p.right
            else:
                temp_p = temp_p.left

        while True:
            if not temp_q:
                ancestors_q = []
                break
            
            ancestors_q.append(temp_q)
            if temp_q.val == q.val:
                break
            elif temp_q.val < q.val:
                temp_q = temp_q.right
            else:
                temp_q = temp_q.left

        ancestors = list(set(ancestors_p).intersection(set(ancestors_q)))
        return ancestors[-1] if ancestors else None


if __name__ == "__main__":
    solution = Solution()
    root = TreeNode.create([6,2,8,0,4,7,9,None,None,3,5])
    print solution.lowestCommonAncestor(root, root.left, root.left.right).val
