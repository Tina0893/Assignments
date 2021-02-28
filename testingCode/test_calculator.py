# -*- coding:utf-8 -*-
import sys

import pytest
import yaml

sys.path.append("..")
from pythonCode.caculator import Calculator


# 数据
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        return (datas["add"]["datas"], datas["add"]["ids"], datas["div"]["datas"], datas["div"]["ids"])


# 测试类
class TestCalc:
    datas: list = get_datas()

    # 前置条件：
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    # 后置条件：
    def teardown_class(self):
        print("计算结束")

    # 相加:
    @pytest.mark.parametrize("a,b,expect", datas[0], ids=datas[1])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)

    # 相除：
    @pytest.mark.parametrize("a,b,expect", datas[2], ids=datas[3])
    def test_div(self, a, b, expect):
        if b == 0:
            try:
                self.calc.div(a, b)
            except Exception as e:
                print("输入错误--除数不能为0")
        else:
            assert expect == self.calc.div(a, b)
