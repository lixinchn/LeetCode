class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        map_islands = {}
        arr_islands = []
        nums = 0
        index = 0
        for i in range(len(grid)):
            line = grid[i]
            for j in range(len(line)):
                island = line[j]
                if island == '1':
                    if i >= 1 and '%s_%s' % (i - 1, j) in map_islands:
                        if grid[i - 1][j] == '1':
                            if '%s_%s' % (i, j) in map_islands:
                                if map_islands['%s_%s' % (i, j)] != map_islands['%s_%s' % (i - 1, j)]:
                                    self.merge(map_islands, arr_islands, map_islands['%s_%s' % (i, j)], map_islands['%s_%s' % (i - 1, j)])
                                    nums -= 1
                            else:
                                map_islands['%s_%s' % (i, j)] = map_islands['%s_%s' % (i - 1, j)]
                                arr_islands[map_islands['%s_%s' % (i, j)]].append('%s_%s' % (i, j))

                    if j < len(line) - 1 and '%s_%s' % (i, j + 1) in map_islands:
                        if grid[i][j + 1] == '1':
                            if '%s_%s' % (i, j) in map_islands:
                                if map_islands['%s_%s' % (i, j)] != map_islands['%s_%s' % (i, j + 1)]:
                                    self.merge(map_islands, arr_islands, map_islands['%s_%s' % (i, j)], map_islands['%s_%s' % (i, j + 1)])
                                    nums -= 1
                            else:
                                map_islands['%s_%s' % (i, j)] = map_islands['%s_%s' % (i, j + 1)]
                                arr_islands[map_islands['%s_%s' % (i, j)]].append('%s_%s' % (i, j))

                    if i < len(grid) - 1 and '%s_%s' % (i + 1, j) in map_islands:
                        if grid[i + 1][j] == '1':
                            if '%s_%s' % (i, j) in map_islands:
                                if map_islands['%s_%s' % (i, j)] != map_islands['%s_%s' % (i + 1, j)]:
                                    self.merge(map_islands, arr_islands, map_islands['%s_%s' % (i, j)], map_islands['%s_%s' % (i + 1, j)])
                                    nums -= 1
                            else:
                                map_islands['%s_%s' % (i, j)] = map_islands['%s_%s' % (i + 1, j)]
                                arr_islands[map_islands['%s_%s' % (i, j)]].append('%s_%s' % (i, j))

                    if j >= 1 and '%s_%s' % (i, j - 1) in map_islands:
                        if grid[i][j - 1] == '1':
                            if '%s_%s' % (i, j) in map_islands:
                                if map_islands['%s_%s' % (i, j)] != map_islands['%s_%s' % (i, j - 1)]:
                                    self.merge(map_islands, arr_islands, map_islands['%s_%s' % (i, j)], map_islands['%s_%s' % (i, j - 1)])
                                    nums -= 1
                            else:
                                map_islands['%s_%s' % (i, j)] = map_islands['%s_%s' % (i, j - 1)]
                                arr_islands[map_islands['%s_%s' % (i, j)]].append('%s_%s' % (i, j))

                    if '%s_%s' % (i, j) not in map_islands:
                        map_islands['%s_%s' % (i, j)] = index
                        arr_islands.append(['%s_%s' % (i, j)])
                        nums += 1
                        index += 1
        return nums

    def merge(self, map_islands, arr_islands, index1, index2):
        index = max(index1, index2)
        min_index = min(index1, index2)
        for key in arr_islands[index]:
            map_islands[key] = min_index
            arr_islands[min_index].append(key)
        arr_islands[index] = []


        
if __name__ == "__main__":
    solution = Solution()
    print solution.numIslands(["11110111111101011111","11111111111011111111","01111101101111111101","11111111111111111101","11110111111110111101","11111011101111111101","11110111111111101111","01011111100101011111","11111111111111111111","11110001011110101111","11111111111111111111","11111111111011110011","01111111111011111111","11111111110111111111","11111011111111111111","11111111111101111011","11111111111111111111","10111011110111111111","11111111111111111111","11011111111111111111"])
    # print solution.numIslands(["111111111","100000001","101010101","101111101","101010101","100000001","111111111"])
    # print solution.numIslands(["1111111","0000001","1111101","1000101","1010101","1011101","1111111"])
    # print solution.numIslands(['11110', '11010', '11000', '00000'])
    # print solution.numIslands(['11000', '11000', '00100', '00011'])
    # print solution.numIslands(['111', '010', '111'])