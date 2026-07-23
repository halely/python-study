"""
写一个支持任意数量数字的计算器
"""
def flexible_calculator(operator: str, *numbers: float, precision: int = 2) -> float | str:
    """
    operator: "+", "-", "*", "/"
    *numbers: 任意多个数字
    precision: 结果保留几位小数
    """
    # 先校验运算符（避免单参数时漏判）
    valid_ops: tuple[str, ...] = ("+", "-", "*", "/")
    if operator not in valid_ops:
        return f"错误：运算符必须为{valid_ops}"

    result: float = numbers[0]
    for n in numbers[1:]:
        if operator == "+":
            result += n
        elif operator == "-":
            result -= n
        elif operator == "*":
            result *= n
        elif operator == "/":
            if n == 0:
                return "错误：不能除以0"
            result /= n
    return f"{result:.{precision}f}"


# 测试
print(flexible_calculator("+", 1, 2, 3, 4))        
print(flexible_calculator("*", 2, 3, 4))            
print(flexible_calculator("/", 10, 2, precision=3)) # 5.000
print(flexible_calculator("/", 10, 0))              # 错误：不能除以0
