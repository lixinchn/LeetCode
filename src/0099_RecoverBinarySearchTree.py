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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        list = []; listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]
            
    def inorder(self, root, list, listp):
        if root:
            self.inorder(root.left, list, listp)
            list.append(root.val); listp.append(root)
            self.inorder(root.right, list, listp)
        
    

if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([3, None, 2, None, 1])
    solution.recoverTree(head)
