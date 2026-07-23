"""
============================================================
Python 学习 — 阶段2 第2课：函数进阶参数
============================================================
本节涵盖：可变参数 *args、关键字参数 **kwargs、
         默认参数陷阱、解包运算符 * 和 **

学习要点：
  1. *args — 接收任意多个位置参数
  2. **kwargs — 接收任意多个关键字参数
  3. 默认参数不要用可变对象（list/dict）
  4. 解包 * / ** — 调用函数时展开序列/字典

运行：python 02_functions/02_function_advanced_args.py
============================================================
"""


# ============================================================
# 1. *args — 接收任意多个位置参数
# ============================================================
def demo_args() -> None:
    print("=" * 40)
    print("1. *args — 接收任意多个位置参数")
    print("=" * 40)

    # 普通函数：只能接收固定参数
    def add_two(a: int, b: int) -> int:
        return a + b

    print(f"add_two(1, 2) = {add_two(1, 2)}")

    # *args：接收任意多个
    def add_all(*numbers: int) -> int:
        """
        *numbers 会把所有多余的位置参数
        打包成一个 tuple
        """
        total: int = 0
        for n in numbers:
            total += n
        return total

    print(f"add_all() = {add_all()}")
    print(f"add_all(1, 2, 3) = {add_all(1, 2, 3)}")
    print(f"add_all(1, 2, 3, 4, 5) = {add_all(1, 2, 3, 4, 5)}")

    # *args 本质上是 tuple
    print(f"*args 内部类型: {type(add_all.__code__)}")  # 函数对象

    # 命名习惯：叫 args 不是强制的，但请遵守约定
    def show_args(*args):
        print(f"args = {args}, type = {type(args)}")

    show_args("a", "b", "c")

    print()


# ============================================================
# 2. **kwargs — 接收任意多个关键字参数
# ============================================================
def demo_kwargs() -> None:
    print("=" * 40)
    print("2. **kwargs — 接收任意多个关键字参数")
    print("=" * 40)

    def create_user(name: str, age: int, **kwargs: object) -> dict:
        """
        **kwargs 会把所有多余的关键字参数
        打包成一个 dict
        """
        user: dict[str, object] = {
            "name": name,
            "age": age,
        }
        # 把额外参数合并进去
        for key, value in kwargs.items():
            user[key] = value
        return user

    user1 = create_user("小明", 15)
    user2 = create_user("小红", 16, city="上海", hobby="画画")

    print(f"user1 = {user1}")
    print(f"user2 = {user2}")

    # kwargs 命名也是约定
    def show_kwargs(**kwargs):
        print(f"kwargs = {kwargs}, type = {type(kwargs)}")

    show_kwargs(a=1, b=2, c="hello")

    print()


# ============================================================
# 3. *args 和 **kwargs 一起用
# ============================================================
def demo_args_kwargs_together() -> None:
    print("=" * 40)
    print("3. *args 和 **kwargs 一起用")
    print("=" * 40)

    def flexible_function(title: str, *tags: str, **metadata: object) -> None:
        """
        参数顺序约定：
        普通位置参数 -> *args -> 普通关键字参数 -> **kwargs
        """
        print(f"标题: {title}")
        print(f"标签: {tags}")
        print(f"元数据: {metadata}")

    flexible_function("Python 学习笔记", "Python", "基础", author="haleLy", date="2026-06-01")

    print()


# ============================================================
# 4. 默认参数陷阱 — 千万不要用可变对象！
# ============================================================
def demo_default_mutable_trap() -> None:
    print("=" * 40)
    print("4. 默认参数陷阱：不要用可变对象！")
    print("=" * 40)

    # ❌ 错误示例：默认参数是空列表
    # Python 的默认参数在函数定义时只创建一次，之后每次调用都共享同一个对象！
    def add_item_bad(item: str, items: list[str] = []) -> list[str]:
        items.append(item)
        return items

    result1 = add_item_bad("苹果")
    result2 = add_item_bad("香蕉")
    print(f"错误示例：result1 = {result1}")  # ['苹果', '香蕉'] ！不是 ['苹果']
    print(f"错误示例：result2 = {result2}")  # ['苹果', '香蕉']
    print(f"它们是同一个对象吗？{result1 is result2}")  # True

    # ✅ 正确做法：默认用 None，函数内部创建新列表
    def add_item_good(item: str, items: list[str] | None = None) -> list[str]:
        if items is None:
            items = []  # 每次调用都创建新列表
        items.append(item)
        return items

    result3 = add_item_good("苹果")
    result4 = add_item_good("香蕉")
    print(f"\n正确示例：result3 = {result3}")  # ['苹果']
    print(f"正确示例：result4 = {result4}")  # ['香蕉']

    print()


# ============================================================
# 5. 解包 * / ** — 调用函数时展开数据
# ============================================================
def demo_unpacking() -> None:
    print("=" * 40)
    print("5. 解包运算符 * 和 **")
    print("=" * 40)

    def introduce(name: str, age: int, city: str) -> str:
        return f"{name}，{age}岁，来自{city}"

    # 用 list/tuple 作为位置参数传入
    person_info = ["小明", 15, "上海"]
    print(f"列表解包: {introduce(*person_info)}")

    # 用 dict 作为关键字参数传入
    person_dict = {"name": "小红", "age": 16, "city": "北京"}
    print(f"字典解包: {introduce(**person_dict)}")

    # 更复杂的组合
    def advanced(a: int, b: int, *args: int, c: int = 10, **kwargs: object) -> None:
        print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

    values = [1, 2, 3, 4]
    config = {"c": 20, "d": 30, "e": 40}
    advanced(*values, **config)
    # 输出：a=1, b=2, args=(3, 4), c=20, kwargs={'d': 30, 'e': 40}

    print()


# ============================================================
# 6. 综合练习：灵活格式化函数
# ============================================================
def demo_practice() -> None:
    print("=" * 40)
    print("6. 综合练习：灵活格式化函数")
    print("=" * 40)

    def format_info(title: str, *items: str, prefix: str = "-", **attrs: object) -> str:
        """
        生成带前缀的列表信息
        title: 标题
        *items: 任意多项内容
        prefix: 列表前缀
        **attrs: 其他属性信息
        """
        lines: list[str] = [f"【{title}】"]
        for item in items:
            lines.append(f"{prefix} {item}")

        if attrs:
            lines.append("---")
            for key, value in attrs.items():
                lines.append(f"{key}: {value}")

        return "\n".join(lines)

    info1 = format_info("购物清单", "牛奶", "面包", "鸡蛋")
    print(info1)
    print()

    info2 = format_info(
        "学习计划",
        "数据类型",
        "循环",
        "字符串",
        prefix="[OK]",
        时间="2小时",
        难度="入门"
    )
    print(info2)

    print()


# ============================================================
if __name__ == "__main__":
    demo_args()
    demo_kwargs()
    demo_args_kwargs_together()
    demo_default_mutable_trap()
    demo_unpacking()
    demo_practice()
