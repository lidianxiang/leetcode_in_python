"""
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""


class Solution:
    """回溯法"""
    def solveSudoku(self, board):

        from collections import defaultdict

        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or \
                        d in boxes[box_index(row, col)])

        def place_number(d, row, col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def remove_number(d, row, col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def place_next_numbers(row, col):
            if col == N - 1 and row == N - 1:
                nonlocal sudoku_solved
                sudoku_solved = True

            else:
                if col == N - 1:
                    backtrack(row + 1, 0)
                else:
                    backtrack(row, col + 1)

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                # 遍历数字1至9
                for d in range(1, 10):
                    # 尝试放入数字d进入(row, col)的格子中
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_numbers(row, col)
                        if not sudoku_solved:
                            # 不能放置，重新放入数字
                            remove_number(d, row, col)
            else:
                # 放置数字
                place_next_numbers(row, col)

        n = 3
        N = n * n
        # 将 9X9 中格子分为9个3X3的小方块
        box_index = lambda row, col: (row // n) * n + col // n

        rows = [defaultdict(int) for _ in range(N)]
        columns = [defaultdict(int) for _ in range(N)]
        boxes = [defaultdict(int) for _ in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d, i, j)
        sudoku_solved = False
        backtrack()

