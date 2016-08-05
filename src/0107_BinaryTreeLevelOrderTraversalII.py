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
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        arr_ret = []
        self.do([root], arr_ret)
        arr_ret.reverse()
        return arr_ret

    def do(self, stack_node, arr_ret):
        if not stack_node:
            return

        arr_num = []
        stack_node_new = []
        for node in stack_node:
            if node and node.val != None:
                arr_num.append(node.val)
            if node.left and node.left.val != None:
                stack_node_new.append(node.left)
            if node.right and node.right.val != None:
                stack_node_new.append(node.right)
        arr_ret.append(arr_num)
        self.do(stack_node_new, arr_ret)

        

if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([3,9,20,None,None,15,7])
    print solution.levelOrderBottom(head)
