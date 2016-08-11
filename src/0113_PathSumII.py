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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        ret_lst = []
        self.do(root, sum, [], ret_lst)
        return ret_lst

    def do(self, root, sum, lst, ret_lst):
        if not root:
            return

        if not root.left and not root.right and root.val == sum:
            lst.append(root.val)
            ret_lst.append(lst)
            return

        if root.left:
            new_lst = lst[:]
            new_lst.append(root.val)
            self.do(root.left, sum - root.val, new_lst, ret_lst)
        if root.right:
            new_lst = lst[:]
            new_lst.append(root.val)
            self.do(root.right, sum - root.val, new_lst, ret_lst)



if __name__ == "__main__":
    solution = Solution()
    head = TreeNode.create([5,4,8,11,1,13,4,7,2,2,2,3,3,5,1])
    print solution.pathSum(head, 22)
