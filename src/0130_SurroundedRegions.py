class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        island_set = {}
        mapping = [[]]
        island_flipping = []

        len_board = len(board)
        island = 1
        board_temp = []
        for i in range(len_board):
            line = []
            board_temp.append(line)
            for j in range(len(board[i])):
                line.append(board[i][j])
                if board[i][j] == 'O':
                    island_top = island_set['%s_%s' % (i - 1, j)] if i - 1 >= 0 and '%s_%s' % (i - 1, j) in island_set else 0
                    island_left = island_set['%s_%s' % (i, j - 1)] if j - 1 >= 0 and '%s_%s' % (i, j - 1) in island_set else 0
                    if not island_top and not island_left:
                        island_min = island
                    elif island_top and island_left:
                        island_min = min(island_top, island_left)
                    elif island_top:
                        island_min = island_top
                    else:
                        island_min = island_left

                    if i == 0 or i == len_board - 1 or j == 0 or j == len(board[i]) - 1:
                        island_flipping.append(island_min)

                    if not island_top and not island_left:
                        island_set['%s_%s' % (i, j)] = island_min
                        mapping.append(['%s_%s' % (i, j)])
                        island += 1
                    elif island_top and island_left:
                        island_set['%s_%s' % (i, j)] = island_min
                        self.adjust_island(island_set, mapping, island_min, island_top, island_left, island_flipping)
                        mapping[island_min].append('%s_%s' % (i, j))
                    elif island_top:
                        island_set['%s_%s' % (i, j)] = island_min
                        mapping[island_min].append('%s_%s' % (i, j))
                    else:
                        island_set['%s_%s' % (i, j)] = island_min
                        mapping[island_min].append('%s_%s' % (i, j))

                    

                    
        island_flipping_set = set(island_flipping)
        for i in range(len(mapping)):
            if not i in island_flipping_set:
                for key in mapping[i]:
                    arr_index = key.split('_')
                    index_i, index_j = int(arr_index[0]), int(arr_index[1])
                    board_temp[index_i][index_j] = 'X'

        for i in range(len(board_temp)):
            line = board_temp[i]
            board[i] = ''.join(line)


    def adjust_island(self, island_set, mapping, island_min, island_top, island_left, island_flipping):
        if island_top != island_min:
            for key in mapping[island_top]:
                mapping[island_min].append(key)
                island_set[key] = island_min
            mapping[island_top] = []
            if island_top in island_flipping:
                island_flipping.append(island_min)
        elif island_left != island_min:
            for key in mapping[island_left]:
                mapping[island_min].append(key)
                island_set[key] = island_min
            if island_left in island_flipping:
                island_flipping.append(island_min)
            mapping[island_left] = []

        
if __name__ == "__main__":
    solution = Solution()
    arr = ["XOXX","OXOX","XOXO","OXOX","XOXO","OXOX"]
    solution.solve(arr)
    print arr

    
    arr = ["OXOOOOOOO","OOOXOOOOX","OXOXOOOOX","OOOOXOOOO","XOOOOOOOX","XXOOXOXOX","OOOXOOOOO","OOOXOOOOO","OOOOOXXOO"]
    solution.solve(arr)
    print arr

    arr = ['XXX', 'XOX', 'XXX']
    solution.solve(arr)
    print arr

    arr = ["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
    solution.solve(arr)
    print arr

    arr = ["XXXXX","XOOOX","XXOOX","XXXOX","XOXXX"]
    solution.solve(arr)
    print arr

    arr = ["OXOOXX","OXXXOX","XOOXOO","XOXXXX","OOXOXX","XXOOOO"]
    solution.solve(arr)
    print arr