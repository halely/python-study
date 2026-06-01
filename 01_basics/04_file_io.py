"""
============================================================
Python 学习 — 阶段1 第4课：文件读写
============================================================
本节涵盖：open()、with 语句、读模式、写模式、逐行处理

学习要点：
  1. with 语句 — 自动关闭文件，不用手动 close()
  2. 读模式 'r' — 读取文件内容
  3. 写模式 'w' — 写入文件（覆盖）
  4. 追加模式 'a' — 追加到文件末尾
  5. 逐行读取 — 处理大文件的标准方式

运行：python 01_basics/04_file_io.py
============================================================
"""
import os
from pathlib import Path

# 临时文件路径（在 01_basics 目录下）
DATA_DIR: Path = Path(__file__).parent
TEMP_FILE: Path = DATA_DIR / "_temp_diary.txt"


# ============================================================
# 1. 写文件 — 'w' 和 'a' 模式
# ============================================================
def demo_write() -> None:
    print("=" * 40)
    print("1. 写文件 (w 模式)")
    print("=" * 40)

    diary_entries: list[str] = [
        "2024-01-15 晴\n",
        "今天学了 Python 的数据类型，列表真好用！\n",
        "2024-01-16 多云\n",
        "循环也不难，多练几次就熟了。\n",
    ]

    # with 语句 — 离开代码块自动关闭文件（即使出错也会关）
    with open(TEMP_FILE, "w", encoding="utf-8") as f:
        f.writelines(diary_entries)          # 写入多行
        f.write("---日记结束---\n")           # 写入单行

    print(f"已写入: {TEMP_FILE}")
    print(f"文件大小: {TEMP_FILE.stat().st_size} 字节")
    print()


# ============================================================
# 2. 读文件 — 三种方式
# ============================================================
def demo_read() -> None:
    print("=" * 40)
    print("2. 读文件")
    print("=" * 40)

    # 方式一：read() — 一次性读入整个文件
    print("--- read() 全部读取 ---")
    with open(TEMP_FILE, "r", encoding="utf-8") as f:
        content: str = f.read()
    print(content)

    # 方式二：readlines() — 按行读入列表
    print("--- readlines() 按行读取（返回列表）---")
    with open(TEMP_FILE, "r", encoding="utf-8") as f:
        lines: list[str] = f.readlines()
    for i, line in enumerate(lines):
        print(f"  第{i}行: {line.rstrip()}")   # rstrip() 去掉行尾换行符

    # 方式三：直接迭代文件对象 — ✅ 处理大文件的标准方式
    print("\n--- 逐行迭代（省内存） ---")
    with open(TEMP_FILE, "r", encoding="utf-8") as f:
        for line in f:                        # 文件对象本身就是可迭代的！
            if "Python" in line:
                print(f"  包含Python的行: {line.strip()}")
    print()


# ============================================================
# 3. 追加模式 'a' — 不覆盖，只追加
# ============================================================
def demo_append() -> None:
    print("=" * 40)
    print("3. 追加模式 (a)")
    print("=" * 40)

    # 用 'a' 模式，不会覆盖已有内容
    with open(TEMP_FILE, "a", encoding="utf-8") as f:
        f.write("2024-01-17 晴转多云\n")
        f.write("今天学了文件读写，Python 确实简洁！\n")
    print("已追加2行")

    # 验证：重新读取看完整内容
    with open(TEMP_FILE, "r", encoding="utf-8") as f:
        print(f"新总行数: {len(f.readlines())}")
    print()


# ============================================================
# 4. 文件模式和路径操作
# ============================================================
def demo_modes_and_path() -> None:
    print("=" * 40)
    print("4. 文件模式一览")
    print("=" * 40)

    print("""
    r   — 只读（文件必须存在）
    w   — 只写（文件不存在则创建，存在则清空）
    a   — 追加（文件不存在则创建，存在则追加到末尾）
    r+  — 读写（文件必须存在）
    x   — 独占创建（文件若存在则报错）
    b   — 二进制模式（配合 rb/wb 用于图片、视频等）
    """)

    # pathlib — 现代路径操作（比 os.path 更推荐）
    print("--- pathlib 路径操作 ---")
    current: Path = Path(".")
    print(f"当前目录: {current.resolve()}")
    print(f"文件名:   {TEMP_FILE.name}")
    print(f"后缀:     {TEMP_FILE.suffix}")
    print(f"父目录:   {TEMP_FILE.parent}")
    print(f"是否存在: {TEMP_FILE.exists()}")
    print()


# ============================================================
# 5. 综合练习：简易日记本
# ============================================================
def diary_app() -> None:
    """
    模拟日记程序：
    - 写日记、读日记、统计日记
    - 综合运用所有文件操作
    """
    print("=" * 40)
    print("5. 综合练习：简易日记本")
    print("=" * 40)

    diary_path: Path = DATA_DIR / "_my_diary.txt"

    # 确保文件存在（首次运行）
    if not diary_path.exists():
        with open(diary_path, "w", encoding="utf-8") as f:
            f.write("=== 我的 Python 学习日记 ===\n\n")

    # 模拟写日记（学习时用 input() 替换）
    simulated_entries: list[tuple[str, str]] = [
        ("2024-01-15", "今天学了 list, tuple, dict, set，信息量不小但很有趣"),
        ("2024-01-16", "循环和判断语句越来越顺手了"),
        ("2024-01-17", "字符串的 f-string 格式化太好用了"),
    ]

    # 追加日记
    print("写日记中...")
    with open(diary_path, "a", encoding="utf-8") as f:
        for date, content in simulated_entries:
            f.write(f"{date}\n")
            f.write(f"  {content}\n")
            f.write("\n")
    print(f"已写入 {len(simulated_entries)} 篇日记\n")

    # 读日记并统计
    print("--- 日记统计 ---")
    total_lines: int = 0
    python_mentions: int = 0

    with open(diary_path, "r", encoding="utf-8") as f:
        for line in f:
            total_lines += 1
            if "Python" in line:
                python_mentions += 1
            if line.startswith("2024"):
                print(f"  [日记] {line.strip()}")

    print(f"\n总行数: {total_lines}")
    print(f"提到 Python 的行数: {python_mentions}")

    # 显示完整日记
    print(f"\n--- 完整日记 ---")
    with open(diary_path, "r", encoding="utf-8") as f:
        print(f.read())

    # 清理（删除临时文件）
    diary_path.unlink(missing_ok=True)
    print("(练习文件已清理)")
    print()


# ============================================================
def cleanup() -> None:
    """删除临时文件"""
    TEMP_FILE.unlink(missing_ok=True)
    print(f"临时文件已清理: {TEMP_FILE.name}")


if __name__ == "__main__":
    demo_write()
    demo_read()
    demo_append()
    demo_modes_and_path()
    diary_app()
    cleanup()
