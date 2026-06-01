"""
============================================================
Python 学习 — 阶段1：核心数据类型
============================================================
本节涵盖：list（列表）、tuple（元组）、dict（字典）、set（集合）

学习要点：
  1. 列表：有序、可变的序列，用 [] 表示
  2. 元组：有序、不可变的序列，用 () 表示
  3. 字典：键值对映射，用 {} 表示
  4. 集合：无序、不重复元素的集合，用 {} 或 set() 表示

先运行本文件看效果：python 01_basics/01_data_types.py
============================================================
"""
from typing import NamedTuple


# ============================================================
# 1. 列表（list）— 最常用的序列类型
# ============================================================
def demo_list() -> None:
    print("=" * 40)
    print("1. 列表 (list)")
    print("=" * 40)

    # 创建列表
    scores: list[int] = [85, 92, 78, 90, 88]
    names: list[str] = ["小明", "小红", "小刚"]
    mixed: list = [1, "hello", 3.14, True]  # 可混合类型（但不推荐）

    print(f"成绩列表: {scores}")
    print(f"第一个成绩: {scores[0]}")          # 索引从 0 开始
    print(f"最后一个成绩: {scores[-1]}")       # 负数索引从尾部开始
    print(f"前三个成绩: {scores[:3]}")         # 切片: [开始:结束]
    print(f"成绩数量: {len(scores)}")          # len() 获取长度

    # 列表操作 — 增删改查
    scores.append(95)                          # 追加到末尾
    print(f"追加后: {scores}")

    scores.insert(1, 100)                      # 在索引1处插入
    print(f"插入后: {scores}")

    scores.remove(78)                          # 按值删除（第一个匹配）
    print(f"删除78后: {scores}")

    popped = scores.pop()                      # 弹出最后一个
    print(f"弹出{popped}后: {scores}")

    # 列表推导式 — Python 的精髓语法
    doubled: list[int] = [s * 2 for s in scores]
    print(f"每项×2: {doubled}")

    passed: list[int] = [s for s in scores if s >= 90]
    print(f"90分以上: {passed}")

    print()


# ============================================================
# 2. 元组（tuple）— 不可变的序列
# ============================================================
def demo_tuple() -> None:
    print("=" * 40)
    print("2. 元组 (tuple)")
    print("=" * 40)

    # 创建元组 — 创建后不能修改
    point: tuple[int, int] = (3, 4)
    rgb: tuple[int, int, int] = (255, 128, 0)
    single: tuple[int, ...] = (42,)           # 单元素元组注意逗号！

    print(f"坐标点: {point}")
    print(f"RGB颜色: {rgb}")
    print(f"x坐标: {point[0]}, y坐标: {point[1]}")

    # 解包（unpacking）— 非常实用的特性
    x, y = point
    print(f"解包: x={x}, y={y}")

    r, g, b = rgb
    print(f"解包RGB: R={r}, G={g}, B={b}")

    # 交换变量 — Python 独有的一行交换
    a, b = 10, 20
    a, b = b, a
    print(f"交换后: a={a}, b={b}")

    # NamedTuple — 有名字的元组（推荐用于结构化数据）
    class Student(NamedTuple):
        name: str
        age: int
        grade: float

    student = Student(name="小明", age=15, grade=92.5)
    print(f"学生: {student.name}, {student.age}岁, 成绩{student.grade}")

    print()


# ============================================================
# 3. 字典（dict）— 键值对映射
# ============================================================
def demo_dict() -> None:
    print("=" * 40)
    print("3. 字典 (dict)")
    print("=" * 40)

    # 创建字典 — 三种常用方式
    student: dict[str, object] = {
        "name": "小明",
        "age": 15,
        "scores": [85, 92, 78],
    }
    print(f"学生信息: {student}")

    empty: dict[str, int] = {}                 # 空字典
    built: dict[str, str] = dict(name="小红", grade="A")  # dict() 构造

    # 访问和修改
    print(f"姓名: {student['name']}")
    print(f"年龄: {student.get('age')}")        # get() 更安全，不存在返回 None
    print(f"电话: {student.get('phone', '未填写')}")  # 设置默认值

    student["phone"] = "13800138000"           # 添加新键值对
    student["age"] = 16                        # 修改已有键的值
    print(f"更新后: {student}")

    # 遍历字典
    print("\n遍历字典:")
    for key, value in student.items():
        print(f"  {key} -> {value}")

    # 字典推导式
    squares: dict[int, int] = {x: x ** 2 for x in range(1, 6)}
    print(f"平方字典: {squares}")

    print()


# ============================================================
# 4. 集合（set）— 无序、不重复
# ============================================================
def demo_set() -> None:
    print("=" * 40)
    print("4. 集合 (set)")
    print("=" * 40)

    # 创建集合 — 自动去重
    numbers: set[int] = {1, 2, 3, 2, 1, 4, 5}
    print(f"创建时自动去重: {numbers}")          # {1, 2, 3, 4, 5}

    empty_set: set[int] = set()                 # 空集合！注意 {} 是空字典

    # 集合操作 — 交、并、差
    math_club: set[str] = {"小明", "小红", "小刚", "小丽"}
    music_club: set[str] = {"小红", "小丽", "小华", "小雪"}

    print(f"\n数学社: {math_club}")
    print(f"音乐社: {music_club}")
    print(f"交集（两个社团都参加）: {math_club & music_club}")
    print(f"并集（所有成员）: {math_club | music_club}")
    print(f"差集（只在数学社）: {math_club - music_club}")
    print(f"对称差（只在其中一个社）: {math_club ^ music_club}")

    # 添加和删除
    math_club.add("小新")
    print(f"\n小新加入数学社: {math_club}")

    # 判断元素是否存在（比列表快得多！）
    print(f"小明在数学社吗？ {'小明' in math_club}")
    print(f"小明在数学社吗？ {'大明' in math_club}")

    print()


# ============================================================
# 5. 综合练习 — 用四种类型解决实际问题
# ============================================================
def comprehensive_exercise() -> None:
    """
    场景：班级成绩分析
    — 用 list 存储成绩
    — 用 tuple 存储不可变的科目信息
    — 用 dict 组织每个学生的数据
    — 用 set 找出需要补考的学生
    """
    print("=" * 40)
    print("5. 综合练习：班级成绩分析")
    print("=" * 40)

    # tuple: 科目列表（固定不变）
    subjects: tuple[str, ...] = ("语文", "数学", "英语")

    # dict: 学生 -> 各科成绩
    class_scores: dict[str, list[int]] = {
        "小明": [88, 92, 85],
        "小红": [75, 60, 78],
        "小刚": [90, 88, 92],
        "小丽": [55, 70, 65],
        "小华": [80, 45, 72],
    }

    # 计算每个学生的平均分（列表推导式遍历 dict）
    print("成绩单:")
    for name, scores in class_scores.items():
        avg = sum(scores) / len(scores)
        print(f"  {name}: {scores} → 平均 {avg:.1f}")

    # 用 set 找出有科目不及格（<60）的学生
    failing_students: set[str] = set()
    for name, scores in class_scores.items():
        for score in scores:
            if score < 60:
                failing_students.add(name)

    print(f"\n需要补考的学生: {failing_students}")

    # 找出所有分数都在80以上的学生（用 all() 函数）
    excellent: set[str] = {
        name for name, scores in class_scores.items()
        if all(s >= 80 for s in scores)
    }
    print(f"全科优秀（都≥80）: {excellent}")
    print()


# ============================================================
# 运行所有示例
# ============================================================
if __name__ == "__main__":
    demo_list()
    demo_tuple()
    demo_dict()
    demo_set()
    comprehensive_exercise()
