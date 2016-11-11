class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP, pathQ = self.findPath(root, p), self.findPath(root, q)
        lenP, lenQ = len(pathP), len(pathQ)
        ans, x = None, 0
        while x < min(lenP, lenQ) and pathP[x] == pathQ[x]:
            ans, x = pathP[x], x + 1
        return ans
        
    def findPath(self, root, target):
        stack = []
        lastVisit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    lastVisit = stack.pop()
                    root = None
        return stack