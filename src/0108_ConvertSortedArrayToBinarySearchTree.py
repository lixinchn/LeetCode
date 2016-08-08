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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.do(nums, 0, len(nums) - 1)

    def do(self, nums, begin, end):
        if begin > end:
            return None

        middle = (begin + end) / 2
        num = nums[middle]
        node = TreeNode(num)
        node.left = self.do(nums, begin, middle - 1)
        node.right = self.do(nums, middle + 1, end)
        return node

if __name__ == "__main__":
    solution = Solution()
    head = solution.sortedArrayToBST([1,2,3,4,5,6,7,8])
    print head