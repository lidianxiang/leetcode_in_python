"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]

"""


class Solution:
    """直接模拟"""
    def fizzBuzz(self, n):
        output = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                output.append('FizzBuzz')
            elif i % 3 == 0 and i % 5 != 0:
                output.append('Fizz')
            elif i % 3 != 0 and i % 5 == 0:
                output.append('Buzz')
            else:
                output.append(str(i))
        return output


class Solution2:
    """
    我们放弃使用之前的联合判断，取而代之依次判断是否能被给定的数整数。
    这道题中，就是依次判断能不能被 3 整除，能不能被 5 整除。
    如果能被 3 整除，就把对应的 Fizz 连接到答案字符串，
    如果能被 5 整除，就把 Buzz 连接到答案字符串。

    条件 1： 15 % 3 == 0, num_ans_str = "Fizz"
    条件 2： 15 % 5 == 0, num_ans_str += "Buzz"
    => num_ans_str = "FizzBuzz"
    """
    def fizzBuzz(self, n):
        output = []
        for num in range(1, n + 1):
            divide_by_3 = num % 3 == 0
            divide_by_5 = num % 5 == 0

            num_str = ""
            if divide_by_3:
                num_str += "Fizz"
            if divide_by_5:
                num_str += "Buzz"
            if not num_str:
                num_str = str(num)
            output.append(num_str)
        return output


class Solution3:
    """散列表，将映射关系放入散列表中，拓展的方向更好，推荐使用第三种形式"""
    def fizzBuzz(self, n):
        output = []
        hash_table = {3: 'Fizz', 5: 'Buzz'}
        for num in range(1, n + 1):
            num_str = ""
            for key in hash_table.keys():
                if num % key == 0:
                    num_str += hash_table[key]

            if not num_str:
                num_str += str(num)
            output.append(num_str)
        return output

