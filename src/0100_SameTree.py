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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            if p.left and q.left:
                if not self.isSameTree(p.left, q.left):
                    return False
            elif p.left and not q.left or not p.left and q.left:
                return False

            if p.right and q.right:
                if not self.isSameTree(p.right, q.right):
                    return False
            elif p.right and not q.right or not p.right and q.right:
                return False
        else:
            return False
        return True
        
    

if __name__ == "__main__":
    solution = Solution()
    head1 = TreeNode.create([3, None, 2, None, 1])
    head2 = TreeNode.create([3, None, 2, None, 1])
    print solution.isSameTree(head1, head2)
