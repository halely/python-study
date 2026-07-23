"""
============================================================
Python 学习 — 阶段2 第4课：异常处理
============================================================
本节涵盖：try/except/else/finally、捕获多种异常、raise、自定义异常

学习要点：
  1. try/except — 捕获错误，不让程序崩溃
  2. else — 没出错时执行
  3. finally — 无论出错与否都执行（清理资源）
  4. raise — 主动抛出异常
  5. 常见异常类型

运行：python 02_functions/04_exception_handling.py
============================================================
"""


# ============================================================
# 1. 没有异常处理的世界 —— 程序直接崩溃
# ============================================================
def demo_without_try() -> None:
    print("=" * 40)
    print("1. 不处理异常 → 程序崩溃")
    print("=" * 40)

    # 模拟用户输入错误（猜数字游戏里的真实场景）
    bad_input: str = "abc"

    # 不处理：下面这行会抛 ValueError，程序崩溃
    try:
        number = int(bad_input)
        print(f"转换成功: {number}")
    except ValueError:
        print(f"不处理的话，这一行就会让程序崩溃: int('{bad_input}')")
        print("→ ValueError: invalid literal for int()")

    print()


# ============================================================
# 2. try/except 基本用法
# ============================================================
def demo_basic_try_except() -> None:
    print("=" * 40)
    print("2. try/except 基本用法")
    print("=" * 40)

    def safe_int_input(text: str) -> int | None:
        """安全的整数转换，出错返回 None 而不是崩溃"""
        user_input: str = input(text)  # 这里用模拟值代替
        try:
            return int(user_input)
        except ValueError:
            print(f"  错误：'{user_input}' 不是有效数字")
            return None

    # 模拟几种输入
    test_inputs = ["42", "abc", "3.14", ""]
    for inp in test_inputs:
        # 临时替换 input 函数来演示
        import builtins
        original_input = builtins.input
        builtins.input = lambda _=inp: inp  # noqa
        result = safe_int_input("请输入: ")
        builtins.input = original_input
        print(f"  输入 '{inp}' → 结果: {result}")

    print()


# ============================================================
# 3. 完整结构：try / except / else / finally
# ============================================================
def demo_full_structure() -> None:
    print("=" * 40)
    print("3. try/except/else/finally 完整结构")
    print("=" * 40)

    def divide(a: float, b: float) -> float | None:
        print(f"\n  尝试计算 {a} / {b}")
        try:
            result: float = a / b           # 可能抛 ZeroDivisionError
        except ZeroDivisionError as e:
            print(f"  except: 捕获到异常 → {e}")
            return None
        except TypeError as e:
            print(f"  except: 类型错误 → {e}")
            return None
        else:
            # else：try 块没抛异常时才执行
            print(f"  else: 计算成功，结果是 {result}")
            return result
        finally:
            # finally：无论是否出错都会执行（清理资源用）
            print(f"  finally: 本次计算结束")

    divide(10, 2)        # 正常
    divide(10, 0)        # 除零错误
    divide("10", 2)      # 类型错误

    print()


# ============================================================
# 4. 捕获多种异常
# ============================================================
def demo_multiple_exceptions() -> None:
    print("=" * 40)
    print("4. 捕获多种异常")
    print("=" * 40)

    def get_list_item(lst: list, index: int):
        """安全地获取列表元素"""
        try:
            return lst[index] / 2
        except IndexError:
            print(f"  索引越界：列表长度{len(lst)}，访问了索引{index}")
            return None
        except TypeError as e:
            print(f"  类型错误：{e}")
            return None
        except ZeroDivisionError:
            print(f"  除零错误")
            return None

    print(f"get_list_item([10, 20], 0) = {get_list_item([10, 20], 0)}")    # 5.0
    print(f"get_list_item([10, 20], 5) = {get_list_item([10, 20], 5)}")    # 越界
    print(f"get_list_item([10, 'x'], 1) = {get_list_item([10, 'x'], 1)}")  # 类型错误

    print()


# ============================================================
# 5. raise — 主动抛出异常
# ============================================================
def demo_raise() -> None:
    print("=" * 40)
    print("5. raise 主动抛出异常")
    print("=" * 40)

    def set_age(age: int) -> None:
        if not isinstance(age, int):
            raise TypeError("年龄必须是整数")
        if age < 0 or age > 150:
            raise ValueError(f"年龄 {age} 不合理（0-150）")
        print(f"  设置年龄成功: {age}")

    # 正常
    set_age(25)

    # 捕获主动抛出的异常
    for bad_age in [-1, 200, "二十"]:
        try:
            set_age(bad_age)  # type: ignore
        except (ValueError, TypeError) as e:
            print(f"  捕获: {type(e).__name__}: {e}")

    print()


# ============================================================
# 6. 自定义异常
# ============================================================
def demo_custom_exception() -> None:
    print("=" * 40)
    print("6. 自定义异常")
    print("=" * 40)

    # 自定义异常：继承 Exception
    class InsufficientFundsError(Exception):
        """余额不足异常"""
        def __init__(self, balance: float, amount: float) -> None:
            self.balance = balance
            self.amount = amount
            super().__init__(
                f"余额不足：当前{balance}元，需要{amount}元，差{amount - balance:.2f}元"
            )

    def withdraw(balance: float, amount: float) -> float:
        if amount > balance:
            raise InsufficientFundsError(balance, amount)
        return balance - amount

    # 测试
    my_balance: float = 100.0
    for amt in [50, 200]:
        try:
            my_balance = withdraw(my_balance, amt)
            print(f"  取款{amt}元成功，剩余{my_balance}元")
        except InsufficientFundsError as e:
            print(f"  取款失败: {e}")

    print()


# ============================================================
# 7. 实战：健壮的猜数字输入
# ============================================================
def demo_robust_input() -> None:
    """解决之前猜数字游戏输入崩溃的问题"""
    print("=" * 40)
    print("7. 实战：健壮的用户输入")
    print("=" * 40)

    def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
        """反复要求输入，直到拿到合法整数"""
        while True:
            try:
                value: int = int(input(prompt))
            except ValueError:
                print("  请输入数字！")
                continue
            if value < min_val or value > max_val:
                print(f"  请输入 {min_val}-{max_val} 之间的数！")
                continue
            return value

    # 模拟测试输入
    import builtins
    test_sequence = ["abc", "0", "15", "7"]  # 故意输错几次，最后输7
    idx = [0]
    def fake_input(_prompt=""):
        val = test_sequence[idx[0]]
        idx[0] += 1
        return val
    builtins.input = fake_input

    result = get_valid_int("猜数字(1-10): ", 1, 10)
    print(f"\n  最终得到合法输入: {result}")

    builtins.input = input  # 恢复
    print()


# ============================================================
if __name__ == "__main__":
    demo_without_try()
    demo_basic_try_except()
    demo_full_structure()
    demo_multiple_exceptions()
    demo_raise()
    demo_custom_exception()
    demo_robust_input()
