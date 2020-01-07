"""
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：

选出任一 x，满足 0 < x < N 且 N % x == 0 。
用 N - x 替换黑板上的数字 N 。
如果玩家无法执行这些操作，就会输掉游戏。

只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回 false。假设两个玩家都以最佳状态参与游戏。

 

示例 1：

输入：2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。
示例 2：

输入：3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
"""


class Solution:
    """
    归纳法

    基本思路：

        1、最终结果应该是占到 2 的赢，占到 1 的输；
        2、若当前为奇数，奇数的约数只能是奇数或者 1，因此下一个一定是偶数；
        3、若当前为偶数， 偶数的约数可以是奇数可以是偶数也可以是 1，因此直接减 1，则下一个是奇数；
        4、因此，奇则输，偶则赢。直接:

    """
    def divisorGame(self, N):
        return N % 2 == 0


class Solution2:
    def divisorGame(self, N):
        target = [0 for _ in range(N + 1)]
        # 若爱丽丝抽到1，则爱丽丝输
        target[1] = 0
        if N <= 1:
            return False
        else:
            # 若爱丽丝抽到2，则爱丽丝赢
            target[2] = 1
            for i in range(3, N + 1):
                for j in range(1, i // 2):
                    # 若j是i的余数 且 target[i-j]为假，则代表当前为真
                    if i % j == 0 and target[i - j] == 0:
                        target[i] = 1
                        break
            return target[N] == 1
