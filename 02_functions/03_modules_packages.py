"""
============================================================
Python 学习 — 阶段2 第3课：模块与包
============================================================
本节涵盖：import 的各种形式、__name__、模块搜索路径、包结构

学习要点：
  1. 模块 = 一个 .py 文件（可被别的文件导入复用）
  2. import 的几种写法
  3. __name__ == "__main__" 的作用
  4. 标准库模块（math / random / datetime）
  5. 包 = 文件夹 + __init__.py

运行：python 02_functions/03_modules_packages.py
============================================================
"""
import random
import math
import datetime

# 导入自定义模块（同目录下的 math_utils.py）
import math_utils
from math_utils import is_prime, factorial, gcd


# ============================================================
# 1. 标准库模块 — Python 自带的工具箱
# ============================================================
def demo_stdlib() -> None:
    print("=" * 40)
    print("1. 标准库模块")
    print("=" * 40)

    # math 模块 — 数学函数
    print(f"math.sqrt(16) = {math.sqrt(16)}")
    print(f"math.pi = {math.pi:.4f}")
    print(f"math.ceil(3.2) = {math.ceil(3.2)}")    # 向上取整
    print(f"math.floor(3.8) = {math.floor(3.8)}")   # 向下取整

    # random 模块 — 随机数
    print(f"\nrandom.randint(1, 100) = {random.randint(1, 100)}")
    fruits = ["苹果", "香蕉", "橘子"]
    print(f"random.choice(fruits) = {random.choice(fruits)}")

    # datetime 模块 — 日期时间
    now = datetime.datetime.now()
    print(f"\n当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    today = datetime.date.today()
    print(f"今天: {today}")

    print()


# ============================================================
# 2. import 的几种写法
# ============================================================
def demo_import_styles() -> None:
    print("=" * 40)
    print("2. import 的几种写法")
    print("=" * 40)

    # 写法一：import 模块名 — 用时要带模块名前缀
    print(f"写法一: math_utils.VERSION = {math_utils.VERSION}")
    print(f"        math_utils.PI = {math_utils.PI:.4f}")

    # 写法二：from 模块 import 名称 — 直接用，不用前缀
    print(f"\n写法二: is_prime(17) = {is_prime(17)}")
    print(f"        factorial(5) = {factorial(5)}")
    print(f"        gcd(12, 8) = {gcd(12, 8)}")

    # 写法三：from 模块 import 名称 as 别名 — 重命名避免冲突
    from math_utils import factorial as fact
    print(f"\n写法三(别名): fact(4) = {fact(4)}")

    # 写法四：import 模块 as 别名
    import math_utils as mu
    print(f"写法四(模块别名): mu.VERSION = {mu.VERSION}")

    # 写法五：from 模块 import * — 导入全部（不推荐！容易命名冲突）
    # from math_utils import *  # 别这么写

    print()


# ============================================================
# 3. __name__ 的魔法
# ============================================================
def demo_dunder_name() -> None:
    print("=" * 40)
    print("3. __name__ 的作用")
    print("=" * 40)

    # 每个模块都有一个特殊变量 __name__
    print(f"本模块的 __name__ = {__name__}")

    # 当直接运行本文件时，__name__ 是 "__main__"
    # 当本文件被别人 import 时，__name__ 是模块名（文件名）
    print(f"math_utils 的 __name__ = {math_utils.__name__}")

    print(f"""
    这就是 if __name__ == "__main__": 的原理：

    if __name__ == "__main__":
        # 只有「直接运行」本文件时才执行
        # 被 import 时不执行
        main()

    好处：
    1. 让文件既能作为模块被导入，又能独立运行测试
    2. 避免 import 时执行不想要的代码
    """)

    print()


# ============================================================
# 4. 模块搜索路径 — Python 去哪儿找模块？
# ============================================================
def demo_search_path() -> None:
    print("=" * 40)
    print("4. 模块搜索路径")
    print("=" * 40)

    import sys

    print("Python 查找模块的顺序：")
    print("  1. 当前目录")
    print("  2. 标准库目录")
    print("  3. 第三方库目录（site-packages）")
    print()
    print("sys.path（搜索路径列表）:")
    for i, path in enumerate(sys.path[:5]):
        print(f"  [{i}] {path}")

    print(f"\n（共 {len(sys.path)} 个路径）")
    print()


# ============================================================
# 5. 包（Package）— 用文件夹组织多个模块
# ============================================================
def demo_package_info() -> None:
    print("=" * 40)
    print("5. 包的概念")
    print("=" * 40)

    print("""
    当项目变大，一个文件装不下时，用「包」组织代码：

    my_project/
    ├── main.py
    └── utils/              ← 这是一个「包」（文件夹）
        ├── __init__.py     ← 包的标志文件（可以为空）
        ├── string_tools.py
        ├── math_tools.py
        └── file_tools.py

    导入方式：
    from utils import string_tools
    from utils.math_tools import add

    __init__.py 的作用：
    - 告诉 Python「这个文件夹是个包」
    - 可以写包初始化代码
    - Python 3.3+ 可以省略，但建议保留（兼容性）

    项目结构建议：
    - 相关功能放一个包
    - 每个模块聚焦单一职责
    - 包名用小写，不用下划线
    """)
    print()


# ============================================================
# 6. pip 与虚拟环境（了解）
# ============================================================
def demo_pip_venv() -> None:
    print("=" * 40)
    print("6. pip 与虚拟环境")
    print("=" * 40)

    print("""
    【pip】— Python 包管理器，安装第三方库
    pip install requests          # 安装
    pip install requests==2.28.0  # 安装指定版本
    pip uninstall requests        # 卸载
    pip list                      # 查看已安装
    pip freeze > requirements.txt # 导出依赖

    常用第三方库：
    - requests   — HTTP 请求
    - pandas     — 数据分析
    - numpy      — 科学计算
    - flask      — Web 框架
    - pytest     — 测试框架

    【虚拟环境】— 隔离不同项目的依赖
    python -m venv venv           # 创建虚拟环境
    venv\\Scripts\\activate          # 激活（Windows）
    source venv/bin/activate      # 激活（Mac/Linux）
    deactivate                    # 退出

    为什么要用虚拟环境？
    - 项目A需要 Django 3，项目B需要 Django 4
    - 互不干扰，各自隔离
    """)
    print()


# ============================================================
if __name__ == "__main__":
    demo_stdlib()
    demo_import_styles()
    demo_dunder_name()
    demo_search_path()
    demo_package_info()
    demo_pip_venv()
