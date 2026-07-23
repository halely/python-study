"""
命令行计算器 — 运算模块
提供加减乘除四个核心运算函数
"""

# ============================================================
# 基础运算函数 — 都支持 *args（任意多个数字）
# ============================================================

def add(*numbers: float) -> float:
    """
    加法：任意多个数字求和
    例：add(1, 2, 3) → 6
    """
    # TODO: 返回所有数字的和
    # 提示：可以用 sum(numbers)
    return sum(numbers)


def subtract(*numbers: float) -> float:
    """
    减法：第一个数减去后面所有数
    例：subtract(100, 20, 30) → 100-20-30 = 50
    """
    result: float = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result


def multiply(*numbers: float) -> float:
    """
    乘法：任意多个数字相乘
    例：multiply(2, 3, 4) → 24
    """
    # TODO: 返回所有数字的乘积
    # 提示：result 初始为 1，循环乘
    result: float = 1
    for num in numbers:
        result *= num
    return result



def divide(*numbers: float) -> float:
    """
    除法：第一个数除以后面所有数
    例：divide(100, 2, 5) → 100/2/5 = 10
    注意：除数为0时抛出异常
    """
    # TODO: 从第一个数开始，依次除以后面的
    # 提示：遇到 0 要 raise ValueError("不能除以0")
    result: float = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ValueError("不能除以0")
        result /= num
    return result
