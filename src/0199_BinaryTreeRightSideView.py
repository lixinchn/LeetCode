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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        same_level_stack = [root]
        next_level_stack = []
        right_most_node = None
        right_list = []

        while True:
            if not same_level_stack or not same_level_stack[0]:
                break

            while same_level_stack:
                node = same_level_stack.pop()
                if node:
                    right_most_node = node
                if node.left and node.left.val != None:
                    next_level_stack.append(node.left)
                if node.right and node.right.val != None:
                    next_level_stack.append(node.right)
            right_list.append(right_most_node.val)
            same_level_stack = next_level_stack
            same_level_stack.reverse()
            next_level_stack = []
        return right_list

        

if __name__ == "__main__":
    solution = Solution()
    node = TreeNode.create([1,2,3,None,4,None,5])
    right_list = solution.rightSideView(node)
    print right_list
