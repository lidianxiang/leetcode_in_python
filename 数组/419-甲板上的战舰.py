"""
给定一个二维的甲板， 请计算其中有多少艘战舰。 战舰用 'X'表示，空位用 '.'表示。 你需要遵守以下规则：

给你一个有效的甲板，仅由战舰或者空位组成。
战舰只能水平或者垂直放置。换句话说,战舰只能由 1xN (1 行, N 列)组成，或者 Nx1 (N 行, 1 列)组成，其中N可以是任意大小。
两艘战舰之间至少有一个水平或垂直的空位分隔 - 即没有相邻的战舰。
示例 :

X..X
...X
...X
在上面的甲板中有2艘战舰。

无效样例 :

...X
XXXX
...X
"""


class Solution:
    def countBattleships(self, board):

        # 判断行与列是否有效
        def is_valid(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
                return False
            else:
                return True

        # 深度优先遍历
        def dfs(row, col):
            # 判断行数和列数是否有效
            if not is_valid(row, col):
                return
            # 当二维数组所指的元素为.(点号)时返回
            if board[row][col] == '.':
                return
            # 将X的上下左右全部变成点号
            board[row][col] = '.'
            dfs(row, col-1)
            dfs(row, col+1)
            dfs(row-1,col)
            dfs(row+1, col)
        # 判断board是否符合条件
        if not board:
            return

        battle_count = 0
        # 按行遍历
        for row in range(len(board)):
            # 按列遍历
            for col in range(len(board[0])):
                if board[row][col] == 'X':
                    battle_count += 1
                    # 深度优先遍历，将X周围全部变成点号
                    dfs(row, col)
        return battle_count
