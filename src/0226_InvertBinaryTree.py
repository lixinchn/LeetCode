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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root

        last_level = [root]
        while last_level:
            this_level = []
            for node in last_level:
                if not node:
                    continue
                this_level.append(node.left)
                this_level.append(node.right)

            if not this_level:
                break

            temp_last_level = this_level[:]
            last_level.reverse()
            for node in last_level:
                if not this_level:
                    break
                if not node:
                    continue

                left_node = this_level.pop()
                right_node = this_level.pop()
                

                node.left = left_node
                node.right = right_node
            last_level = temp_last_level
        return root


if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([2,3,None,1])
    root = solution.invertTree(head)
