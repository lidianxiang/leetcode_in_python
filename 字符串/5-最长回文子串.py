"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""


class Solution:
    """暴力解法，O(n^3)的时间复杂度，思路清晰但是leetcode会超过时间限制"""
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(size - 1):
            for j in range(i + 1, size):
                if j - i + 1 > max_len and self._valid(s, i, j):
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res

    def _valid(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    """
    中心扩散法：
        1、遍历每一个索引，以这个索引为中心，利用回文串中心对称的特点，往两边扩散，看最多能扩散多远
        2、时间复杂度为O(n^2):遍历的时间复杂度为O(n),从中心位置扩散得到的回文子串的时间复杂度为O(n)
        3、值得注意的是，需要考虑到回文串的长度为奇数与偶数的情况

    """
    def longestPalindrome(self,  s):
        size = len(s)
        if size < 2:
            return s

        max_len = 1
        res = s[0]

        for i in range(size):
            # 回文中心为奇数
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            # 回文中心为偶数
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
            # 判断最大长度为奇数还是偶数
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            # 更新最大子串长度
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res

    def __center_spread(self, s, size, left, right):
        """
        left = right的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        i, j = left, right
        while i >= 0 and j < size and s[i] == s[j]:
            # 由中心向两边扩散
            i -= 1
            j += 1
        return s[i + 1: j], j - i - 1


class Solution3:
    """
    Manacher算法（基于中心扩散法）采用和kmp算法类似的思想，时间复杂度为O(n)

    首先在字符串的首尾、相邻的字符中插入分隔符，例如 "babad" 添加分隔符 "#" 以后得到 "#b#a#b#a#d#"。

    对这一点有如下说明：

        1、分隔符是一个字符，种类也只有一个，并且这个字符一定不能是原始字符串中出现过的字符；

        2、加入了分隔符以后，使得“间隙”有了具体的位置，方便后续的讨论，并且新字符串中的任意一个回文子串在原始字符串中的一定能找到唯一的一个回文子串与之对应，因此对新字符串的回文子串的研究就能得到原始字符串的回文子串；

        3、新字符串的回文子串的长度一定是奇数；

        4、新字符串的回文子串一定以分隔符作为两边的边界，因此分隔符起到“哨兵”的作用。
    """
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s

        t = '#'
        for i in range(size):
            t += s[i]
            t += '#'
        # 加入#后的字符串的长度
        t_len = 2 * size + 1

        max_len = 1
        start = 0

        for i in range(t_len):
            cur_len = self.__center_spread(t, i)
            if cur_len > max_len:
                max_len = cur_len
                # 再次开始的start的长度
                start = (i - max_len) // 2
        return s[start: start + max_len]

    def __center_spread(self, s, center):
        size = len(s)
        i = center - 1
        j = center + 1
        step = 0
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
            # step为对称的的长度
            step += 1
        return step


class Solution4:
    """
    动态规划：
        1、定义状态
        2、找到状态转移方程
    """
    def longestPalindrome(self, s):
        size = len(s)
        # 特殊条件判断
        if size < 2:
            return s
        # 初始化二维布尔数组dp
        dp = [[False for _ in range(size)] for _ in range(size)]
        # 初始化最长的回文串长度为1
        longest_l = 1
        res = s[0]

        for r in range(1, size):
            for l in range(r):
                # 当左右边界的字符相等的同时，满足：当去掉左右边界时不构成区间或者去掉左右边界的字符串仍是回文串
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    # 判断最长回文串是否需要更新
                    if cur_len > longest_l:
                        longest_l = cur_len
                        # 回文串的位置
                        res = s[l:r + 1]
        return res
