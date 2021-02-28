# -*- coding:utf-8 -*-

# 被测试代码：计算器加法、除法


class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b == 0:
            print("除数不能为0")
        else:
            return a / b
