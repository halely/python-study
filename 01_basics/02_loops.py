"""
============================================================
Python 学习 — 阶段1 第2课：循环
============================================================
本节涵盖：for 循环、while 循环、break、continue、else 子句

学习要点：
  1. for 循环 — 遍历序列中的每个元素
  2. while 循环 — 满足条件时持续执行
  3. break — 提前终止循环
  4. continue — 跳过当前迭代，进入下一轮
  5. for/while 的 else 子句 — Python 独有的特性

运行：python 01_basics/02_loops.py
============================================================
"""
import random


# ============================================================
# 1. for 循环 — 遍历一切可迭代对象
# ============================================================
def demo_for_loop() -> None:
    print("=" * 40)
    print("1. for 循环")
    print("=" * 40)

    # 遍历列表
    fruits: list[str] = ["苹果", "香蕉", "橘子", "葡萄"]
    print("遍历列表:")
    for fruit in fruits:
        print(f"  吃一个: {fruit}")

    # 遍历字符串（字符串也是序列！）
    print("\n遍历字符串:")
    for char in "Python":
        print(f"  字母: {char}")

    # range() — 生成数字序列
    print("\nrange(5):", end=" ")
    for i in range(5):                # 0, 1, 2, 3, 4
        print(i, end=" ")

    print("\nrange(2, 7):", end=" ")
    for i in range(2, 7):             # 2, 3, 4, 5, 6
        print(i, end=" ")

    print("\nrange(1, 10, 2):", end=" ")
    for i in range(1, 10, 2):         # 1, 3, 5, 7, 9（步长为2）
        print(i, end=" ")

    # enumerate() — 同时获取索引和值
    print("\n\n带索引遍历:")
    for index, fruit in enumerate(fruits):
        print(f"  [{index}] {fruit}")

    # zip() — 同时遍历多个序列（配对）
    print("\n同时遍历两个列表:")
    names: list[str] = ["小明", "小红", "小刚"]
    scores: list[int] = [85, 92, 78]
    for name, score in zip(names, scores):
        print(f"  {name}: {score}分")

    print()


# ============================================================
# 2. while 循环 — 条件驱动的循环
# ============================================================
def demo_while_loop() -> None:
    print("=" * 40)
    print("2. while 循环")
    print("=" * 40)

    # 基本 while — 当条件为 True 时持续执行
    print("倒计时:")
    countdown: int = 5
    while countdown > 0:
        print(f"  {countdown}...")
        countdown -= 1               # 别忘了改变条件，否则死循环！
    print("  发射！")

    # while True + break — 无限循环配合退出条件
    print("\n累积求和（输入0结束）:")
    total: int = 0
    # 模拟用户输入（实际学习中用 input()）
    simulated_inputs: list[int] = [10, 20, 5, 0, 30]
    for num in simulated_inputs:
        if num == 0:
            break
        total += num
        print(f"  加了 {num}，当前总和: {total}")
    print(f"  最终结果: {total}")

    print()


# ============================================================
# 3. break 和 continue — 循环控制
# ============================================================
def demo_break_continue() -> None:
    print("=" * 40)
    print("3. break 和 continue")
    print("=" * 40)

    # break — 完全退出循环
    print("找到目标就停止:")
    numbers: list[int] = [3, 7, 2, 9, 5, 8]
    for num in numbers:
        if num == 9:
            print(f"  找到了！数字 {num} 在第 {numbers.index(num)} 位")
            break                        # 找到就停，不继续找了
        print(f"  检查 {num}...不是它")

    # continue — 跳过当前迭代
    print("\n跳过偶数:")
    for num in range(1, 11):
        if num % 2 == 0:
            continue                     # 偶数跳过，不打印
        print(f"  {num}（奇数）")

    print()


# ============================================================
# 4. for/while 的 else 子句 — Python 独有！
# ============================================================
def demo_loop_else() -> None:
    """
    Python 中循环可以带 else：
    - 循环正常结束（没有被 break 中断）→ 执行 else
    - 循环被 break 中断 → 不执行 else
    这个特性其他语言很少见！
    """
    print("=" * 40)
    print("4. 循环的 else 子句（Python 独有）")
    print("=" * 40)

    # 场景：找素数
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"    {n} 能被 {i} 整除，不是素数")
                break                # break → 不执行 else
        else:                        # for 循环正常结束 → 执行 else
            print(f"    {n} 是素数！")
            return True
        return False

    print("判断素数:")
    is_prime(17)    # 素数
    is_prime(24)    # 非素数
    is_prime(7)     # 素数

    print()


# ============================================================
# 5. 综合练习：猜数字游戏
# ============================================================
def guess_number_game() -> None:
    """
    猜数字游戏 — 综合运用:
    - while 循环（持续猜直到猜中/放弃）
    - for 循环 + break（限制次数）
    - range()、条件判断
    - random 模块生成随机数
    """
    print("=" * 40)
    print("5. 综合练习：猜数字游戏")
    print("=" * 40)

    target: int = random.randint(1, 10)    # 1-10 随机数
    max_attempts: int = 5

    print(f"我想了一个 1-10 之间的数字，你有 {max_attempts} 次机会！")

    # 模拟猜数过程（学习时用 input() 替换）
    simulated_guesses: list[int] = [5, 2, 8, target]  # 第4次猜中

    for attempt, guess in enumerate(simulated_guesses, start=1):
        print(f"\n第 {attempt} 次猜测: {guess}")

        if guess < target:
            print("  太小了！往上猜")
        elif guess > target:
            print("  太大了！往下猜")
        else:
            print(f"  *** 恭喜猜中！答案就是 {target}，你用了 {attempt} 次")
            break
    else:
        # for 循环没被 break → 所有次数用完
        print(f"\n  :( 游戏结束，答案是 {target}")

    print()


# ============================================================
# 运行所有示例
# ============================================================
if __name__ == "__main__":
    demo_for_loop()
    demo_while_loop()
    demo_break_continue()
    demo_loop_else()
    guess_number_game()
