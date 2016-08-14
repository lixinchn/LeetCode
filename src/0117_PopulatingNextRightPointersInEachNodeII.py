class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

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
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        self.do(root, None, None)

    def do(self, root, next, next_parent):
        if not root:
            return
        root.next = next
        if not root.next and next_parent:
            while next_parent:
                if next_parent.left:
                    root.next = next_parent.left
                    break
                if next_parent.right:
                    root.next = next_parent.right
                    break
                next_parent = next_parent.next
        self.do(root.right, root.next.left if root.next else None, root.next)
        self.do(root.left, root.right, root.next)



if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([1,2,3,4,5,None,7])
    solution.connect(head)
    print head