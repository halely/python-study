"""
============================================================
Python 学习 — 阶段1 第3课：字符串操作
============================================================
本节涵盖：字符串切片、常用方法、f-string 格式化、split/join

学习要点：
  1. 字符串切片 — 和列表一样用 [start:end:step]
  2. 常用方法 — upper/lower/strip/replace/find/startswith/endswith
  3. f-string — Python 3.6+ 最推荐的格式化方式
  4. split/join — 字符串和列表互转的核心工具

运行：python 01_basics/03_strings.py
============================================================
"""


# ============================================================
# 1. 字符串切片 — 和列表切片完全一样
# ============================================================
def demo_string_slicing() -> None:
    print("=" * 40)
    print("1. 字符串切片")
    print("=" * 40)

    text: str = "Hello Python!"
    print(f"原始字符串: '{text}'")
    print(f"长度: {len(text)}")
    print()

    # 索引（和列表一样从 0 开始）
    print(f"text[0]  = '{text[0]}'")      # 第一个字符
    print(f"text[-1] = '{text[-1]}'")     # 最后一个字符
    print(f"text[6]  = '{text[6]}'")      # 第7个字符

    # 切片 [start:end] — 不包含 end
    print(f"\ntext[0:5]  = '{text[0:5]}'")    # 前5个字符
    print(f"text[:5]   = '{text[:5]}'")       # 省略 start = 从头开始
    print(f"text[6:]   = '{text[6:]}'")       # 省略 end = 到末尾
    print(f"text[:]    = '{text[:]}'")        # 全部（复制）

    # 步长 [start:end:step]
    print(f"\ntext[::2]  = '{text[::2]}'")    # 每隔一个字符
    print(f"text[::-1] = '{text[::-1]}'")     # 反转字符串！

    # 不可变性 — 字符串不能原地修改
    print("\n字符串不可变:")
    try:
        text[0] = "h"  # 这会报错！
    except TypeError as e:
        print(f"  text[0] = 'h' → {e}")
    print("  正确做法: new_text = 'h' + text[1:]")
    print(f"  结果: '{'h' + text[1:]}'")

    print()


# ============================================================
# 2. 常用字符串方法 — 这些每天都会用到
# ============================================================
def demo_string_methods() -> None:
    print("=" * 40)
    print("2. 常用字符串方法")
    print("=" * 40)

    raw: str = "  Hello Python World!  "
    print(f"原始: '{raw}'")

    # 大小写转换
    print(f"\n--- 大小写 ---")
    print(f"upper():  '{raw.upper()}'")
    print(f"lower():  '{raw.lower()}'")
    print(f"title():  '{raw.title()}'")       # 每个单词首字母大写
    print(f"capitalize(): '{raw.capitalize()}'")  # 首字母大写

    # 去除空白
    print(f"\n--- 去除空白 ---")
    print(f"strip():  '{raw.strip()}'")       # 去两端空白
    print(f"lstrip(): '{raw.lstrip()}'")      # 去左边空白
    print(f"rstrip(): '{raw.rstrip()}'")      # 去右边空白

    # 查找和替换
    text: str = "apple banana apple orange"
    print(f"\n--- 查找和替换 ---")
    print(f"find('apple'):   {text.find('apple')}")      # 首次出现的位置
    print(f"find('grape'):   {text.find('grape')}")      # 找不到返回 -1
    print(f"count('apple'):  {text.count('apple')}")     # 出现次数
    print(f"replace:        '{text.replace('apple', 'grape')}'")  # 全部替换
    print(f"replace 1次:    '{text.replace('apple', 'grape', 1)}'")  # 只替换第1个

    # 判断方法（返回 True/False）
    print(f"\n--- 判断 ---")
    print(f"'abc'.isalpha():   {'abc'.isalpha()}")    # 全是字母？
    print(f"'123'.isdigit():   {'123'.isdigit()}")    # 全是数字？
    print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")  # 字母+数字？
    print(f"'  '.isspace():    {'  '.isspace()}")     # 全是空白？
    print(f"startswith('Hel'): {raw.strip().startswith('Hel')}")
    print(f"endswith('!'):     {raw.strip().endswith('!')}")

    print()


# ============================================================
# 3. f-string — Python 最强大的字符串格式化
# ============================================================
def demo_fstring() -> None:
    print("=" * 40)
    print("3. f-string 格式化")
    print("=" * 40)

    name: str = "小明"
    age: int = 15
    score: float = 92.567

    # 基本用法 — 直接嵌入变量
    print(f"我叫{name}，今年{age}岁")

    # 数字格式化
    print(f"分数: {score:.1f}")          # 保留1位小数 → 92.6
    print(f"分数: {score:.2f}")          # 保留2位小数 → 92.57
    print(f"百分比: {0.856:.1%}")        # 百分比格式 → 85.6%
    print(f"千分位: {1234567:,}")        # 逗号分隔 → 1,234,567

    # 对齐和填充
    print(f"\n--- 对齐 ---")
    print(f"|{'左对齐':<10}|")           # < 左对齐，宽度10
    print(f"|{'居中':^10}|")             # ^ 居中，宽度10
    print(f"|{'右对齐':>10}|")           # > 右对齐，宽度10
    print(f"|{'填充':-^10}|")            # 用 - 填充 → |----填充----|

    # 表达式 — 花括号里可以直接写表达式！
    print(f"\n--- 表达式 ---")
    a, b = 10, 3
    print(f"{a} + {b} = {a + b}")
    print(f"{a} / {b} = {a / b:.2f}")
    print(f"年龄明年: {age + 1}")

    # 调试模式 (Python 3.8+) — 变量名=值 一起输出
    print(f"\n--- 调试 ---")
    print(f"{name = }")                 # 输出 name = '小明'
    print(f"{a + b = }")                # 输出 a + b = 13

    # 对比三种格式化方式（了解即可，优先用 f-string）
    print(f"\n--- 三种格式化对比 ---")
    print(f"f-string:    f'{name} {age}岁'")       # ✅ 推荐
    print("str.format:  '{} {}岁'.format(name, age)")   # ⚠️ 旧风格
    print("百分号:      '%s %d岁' % (name, age)")        # ❌ 更旧，别用

    print()


# ============================================================
# 4. split 和 join — 字符串 ↔ 列表互转
# ============================================================
def demo_split_join() -> None:
    print("=" * 40)
    print("4. split 和 join")
    print("=" * 40)

    # split — 字符串 → 列表（按分隔符切开）
    csv_line: str = "小明,15,92.5,上海"
    parts: list[str] = csv_line.split(",")
    print(f"split(','): '{csv_line}' → {parts}")

    sentence: str = "Python is fun to learn"
    words: list[str] = sentence.split()     # 默认按空白分割
    print(f"split(): '{sentence}' → {words}")

    limited: list[str] = sentence.split(" ", 2)  # 只分2次
    print(f"split(' ', 2): → {limited}")

    # join — 列表 → 字符串（用分隔符粘合）
    print(f"\njoin:")
    words_again: list[str] = ["Python", "is", "awesome"]
    print(f"' '.join({words_again}) → '{' '.join(words_again)}'")
    print(f"','.join({words_again}) → '{','.join(words_again)}'")
    print(f"'|'.join({words_again}) → '{'|'.join(words_again)}'")
    print(f"''.join({words_again}) → '{''.join(words_again)}'")  # 直接拼接

    print()


# ============================================================
# 5. 综合练习：文本统计分析器
# ============================================================
def text_analyzer() -> None:
    """
    场景：分析一段文本的统计信息
    - split 分词
    - count 统计
    - f-string 格式化输出
    """
    print("=" * 40)
    print("5. 综合练习：文本统计分析")
    print("=" * 40)

    article: str = (
        "Python was created by Guido van Rossum. "
        "Python is easy to learn. "
        "Many people love Python because Python is powerful. "
        "Python Python Python!"
    )
    print(f"原文:\n  {article}\n")

    # 分词
    words: list[str] = article.lower().replace(".", "").replace("!", "").split()
    print(f"总词数: {len(words)}")

    # 不重复的词（用 set 去重！）
    unique: set[str] = set(words)
    print(f"不重复词数: {len(unique)}")
    print(f"词汇表: {sorted(unique)}")

    # 词频统计（用字典）
    word_count: dict[str, int] = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print(f"\n词频统计:")
    # 按词频排序显示（lambda 是匿名函数，后面会学）
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words[:5]:  # 取前5个
        bar: str = "*" * count
        print(f"  {word:<10} {count:>2} {bar}")

    # 字符串统计
    print(f"\n字符统计:")
    print(f"  总字符数: {len(article)}")
    print(f"  不含空格: {len(article.replace(' ', ''))}")
    print(f"  大写P出现次数: {article.count('P')}")
    print(f"  'Python'出现次数: {article.count('Python')}")

    print()


# ============================================================
if __name__ == "__main__":
    demo_string_slicing()
    demo_string_methods()
    demo_fstring()
    demo_split_join()
    text_analyzer()
