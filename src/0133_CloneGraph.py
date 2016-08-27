class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        ret = None
        if node:
            ret = self.dfs(node, {})
        return ret

    def dfs(self, node, map_node):
        if node in map_node:
            return map_node[node]
        output = UndirectedGraphNode(node.label)
        map_node[node] = output
        for neighbor in node.neighbors:
            output.neighbors.append(self.dfs(neighbor, map_node))
        return output


if __name__ == "__main__":
    solution = Solution()
    a = UndirectedGraphNode('a')
    b = UndirectedGraphNode('b')
    c = UndirectedGraphNode('c')
    a.neighbors = [b, c]
    b.neighbors = [a]
    c.neighbors = [c]
    print solution.cloneGraph(a)
