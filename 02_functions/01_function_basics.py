"""
============================================================
Python 学习 — 阶段2 第1课：函数基础
============================================================
本节涵盖：函数定义、参数、返回值、作用域、lambda

学习要点：
  1. def — 定义可复用的代码块
  2. return — 返回值、多返回值、无返回值
  3. 参数 — 位置参数、关键字参数
  4. 作用域 — LEGB 规则、global 关键字
  5. lambda — 简单匿名函数

运行：python 02_functions/01_function_basics.py
============================================================
"""


# ============================================================
# 1. 函数定义与调用
# ============================================================
def demo_define_call() -> None:
    print("=" * 40)
    print("1. 函数定义与调用")
    print("=" * 40)

    # 最简单的函数
    def say_hello() -> None:
        print("Hello, Python!")

    say_hello()  # 调用函数

    # 带参数的函数
    def greet(name: str) -> None:
        print(f"你好，{name}！")

    greet("小明")  # 位置参数
    greet(name="小红")  # 关键字参数

    # 带返回值的函数
    def add(a: int, b: int) -> int:
        return a + b

    result: int = add(3, 5)
    print(f"3 + 5 = {result}")

    print()


# ============================================================
# 2. 多返回值 — Python 用 tuple 自动打包
# ============================================================
def demo_multiple_returns() -> None:
    print("=" * 40)
    print("2. 多返回值")
    print("=" * 40)

    def get_circle_info(radius: float) -> tuple[float, float]:
        """返回圆的周长和面积"""
        perimeter: float = 2 * 3.14159 * radius
        area: float = 3.14159 * radius ** 2
        return perimeter, area  # Python 自动打包成 tuple

    p, a = get_circle_info(5.0)  # 解包接收多个返回值
    print(f"半径为5的圆：周长={p:.2f}，面积={a:.2f}")

    # 也可以用一个变量接收整个 tuple
    info = get_circle_info(3.0)
    print(f"完整返回: {info}")

    print()


# ============================================================
# 3. 参数传递方式
# ============================================================
def demo_arguments() -> None:
    print("=" * 40)
    print("3. 参数传递方式")
    print("=" * 40)

    def describe_pet(animal: str, name: str, age: int = 1) -> None:
        """
        animal, name 是位置参数
        age=1 是默认参数
        """
        print(f"我有一只{animal}，名字叫{name}，{age}岁")

    # 位置参数
    describe_pet("狗", "旺财")

    # 关键字参数（可以打乱顺序）
    describe_pet(name="咪咪", animal="猫", age=2)

    # 混合使用：位置参数在前，关键字参数在后
    describe_pet("兔子", name="小白", age=3)

    # 关键字参数尤其重要：让调用意图更明确
    describe_pet("乌龟", "阿龟", 50)      # 50是什么？年龄？体重？
    describe_pet(animal="乌龟", name="阿龟", age=50)  # 清晰多了！

    print()


# ============================================================
# 4. 作用域 — LEGB 规则
# ============================================================
def demo_scope() -> None:
    print("=" * 40)
    print("4. 作用域")
    print("=" * 40)

    message: str = "我在外部（demo_scope的局部变量）"

    def outer() -> None:
        message: str = "我在外层函数"

        def inner() -> None:
            message: str = "我在内层函数"
            print(f"inner: {message}")  # 内层变量

        inner()
        print(f"outer: {message}")      # 外层变量

    outer()
    print(f"demo_scope: {message}")     # demo_scope 的局部变量

    # Python 的 LEGB 查找顺序：
    # Local（局部） -> Enclosing（嵌套） -> Global（全局） -> Built-in（内置）

    print()


# global 关键字 — 慎用！用于在函数内部修改全局变量
counter: int = 0


def increment() -> None:
    global counter
    counter += 1


def demo_global() -> None:
    print("=" * 40)
    print("4.1 global 关键字")
    print("=" * 40)

    global counter
    print(f"初始 counter = {counter}")

    increment()
    increment()
    increment()
    print(f"调用3次后 counter = {counter}")

    # 更好的做法：避免 global，用参数和返回值
    def increment_local(value: int) -> int:
        return value + 1

    local_count: int = 0
    local_count = increment_local(local_count)
    local_count = increment_local(local_count)
    print(f"不使用 global: {local_count}")

    print()


# ============================================================
# 5. lambda 匿名函数
# ============================================================
def demo_lambda() -> None:
    print("=" * 40)
    print("5. lambda 匿名函数")
    print("=" * 40)

    # lambda 适合定义简单、只用一次的函数
    square = lambda x: x ** 2
    print(f"square(5) = {square(5)}")

    # lambda 经常配合 sorted 使用
    students: list[tuple[str, int]] = [
        ("小明", 85),
        ("小红", 92),
        ("小刚", 78),
    ]

    # 按分数排序（sorted 函数的 key 参数）
    sorted_by_score = sorted(students, key=lambda s: s[1], reverse=True)
    print(f"按分数排序: {sorted_by_score}")

    # 普通函数版本（可读性更好，lambda 只用于简单场景）
    def get_score(student: tuple[str, int]) -> int:
        return student[1]

    sorted_by_score_2 = sorted(students, key=get_score)
    print(f"按分数排序2: {sorted_by_score_2}")

    print()


# ============================================================
# 6. 文档字符串与 help
# ============================================================
def demo_docstring() -> None:
    print("=" * 40)
    print("6. 文档字符串")
    print("=" * 40)

    def calculate_bmi(height: float, weight: float) -> float:
        """
        计算 BMI 指数。

        参数:
            height: 身高，单位厘米
            weight: 体重，单位公斤

        返回:
            BMI 值，保留两位小数
        """
        bmi: float = weight / ((height / 100) ** 2)
        return round(bmi, 2)

    print(f"BMI = {calculate_bmi(175, 70)}")

    # 查看函数文档
    print("\n函数文档:")
    print(calculate_bmi.__doc__)

    print()


# ============================================================
# 7. 综合练习：简单计算器函数
# ============================================================
def simple_calculator() -> None:
    """用函数重构一个简单的四则运算计算器"""
    print("=" * 40)
    print("7. 综合练习：函数版计算器")
    print("=" * 40)

    def add(a: float, b: float) -> float:
        return a + b

    def subtract(a: float, b: float) -> float:
        return a - b

    def multiply(a: float, b: float) -> float:
        return a * b

    def divide(a: float, b: float) -> float | None:
        if b == 0:
            print("错误：不能除以0")
            return None
        return a / b

    x, y = 10.0, 3.0
    print(f"{x} + {y} = {add(x, y)}")
    print(f"{x} - {y} = {subtract(x, y)}")
    print(f"{x} * {y} = {multiply(x, y)}")
    print(f"{x} / {y} = {divide(x, y)}")
    print(f"{x} / 0 = {divide(x, 0)}")

    print()


# ============================================================
if __name__ == "__main__":
    demo_define_call()
    demo_multiple_returns()
    demo_arguments()
    demo_scope()
    demo_global()
    demo_lambda()
    demo_docstring()
    simple_calculator()
