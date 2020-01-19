"""
你正在和你的朋友玩 猜数字（Bulls and Cows）游戏：你写下一个数字让你的朋友猜。每次他猜测后，你给他一个提示，告诉他有多少位数字和确切位置都猜对了（称为“Bulls”, 公牛），有多少位数字猜对了但是位置不对（称为“Cows”, 奶牛）。你的朋友将会根据提示继续猜，直到猜出秘密数字。

请写出一个根据秘密数字和朋友的猜测数返回提示的函数，用 A 表示公牛，用 B 表示奶牛。

请注意秘密数字和朋友的猜测数都可能含有重复数字。

示例 1:

输入: secret = "1807", guess = "7810"

输出: "1A3B"

解释: 1 公牛和 3 奶牛。公牛是 8，奶牛是 0, 1 和 7。
示例 2:

输入: secret = "1123", guess = "0111"

输出: "1A1B"

解释: 朋友猜测数中的第一个 1 是公牛，第二个或第三个 1 可被视为奶牛。
"""


class Solution:
    def getHint(self, secret, guess):
        from collections import Counter
        s_c = Counter(secret)
        g_c = Counter(guess)
        res = [0, 0]
        for x, y in zip(secret, guess):
            # 位置和数字都相同的情况
            if x == y:
                s_c[x] -= 1
                g_c[y] -= 1
                res[0] += 1
        # 数字相同，但是位置不同的情况
        for k in s_c & g_c:
            res[1] += min(s_c[k], g_c[k])
        return "{}A{}B".format(res[0], res[1])


class Solution2:
    """不使用collections.Counter()函数，单纯使用字典"""
    def getHint(self, secret, guess):
        A, B = 0, 0
        dic_1, dic_2 = {}, {}
        size = len(secret)
        for i in range(size):
            # 位置和数字都相同的情况
            if secret[i] == guess[i]:
                A += 1
            # 数字相同，但是位置不同的情况，分别存入两个字典中
            else:
                if secret[i] not in dic_1:
                    dic_1[secret[i]] = 1
                else:
                    dic_1[secret[i]] += 1

                if guess[i] not in dic_2:
                    dic_2[guess[i]] = 1
                else:
                    dic_2[guess[i]] += 1
        for x in dic_1:
            if x in dic_2:
                B += min(dic_1[x], dic_2[x])
        return str(A) + 'A' + str(B) + 'B'
