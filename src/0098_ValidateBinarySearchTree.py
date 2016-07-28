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
    def ValidBST(self, root, min, max):
        if root == None:
            return True
        if (min != None and root.val <= min) or (max != None and root.val >= max):
            return False
        return self.ValidBST(root.left, min, root.val) and self.ValidBST(root.right, root.val, max)
    
    def isValidBST(self, root):
        return self.ValidBST(root, None, None)


if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([10,5,15,None,None,6,20])
    print solution.isValidBST(head)

    head = TreeNode.create([2,1,3])
    print solution.isValidBST(head)

    head = TreeNode.create([[2147483647]])
    print solution.isValidBST(head)

    head = TreeNode.create([0, None, -1])
    print solution.isValidBST(head)