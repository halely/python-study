"""
命令行计算器 — 主程序
整合：菜单循环 + 历史记录 + 异常处理
"""
import calculator_ops as calc


# ============================================================
# 工具函数
# ============================================================

def get_numbers(prompt: str = "请输入数字（用空格分隔）: ") -> list[float]:
    """
    获取用户输入的一行数字，用空格分隔
    返回浮点数列表；输入非法时反复要求
    """
    while True:
        raw: str = input(prompt).strip()
        try:
            # TODO: 把 "1 2 3" 转成 [1.0, 2.0, 3.0]
            # 提示：用 split() 分割，再用列表推导式 float(x)
            numbers = [float(x) for x in raw.split()]
            if not numbers:
                print("  至少输入一个数字")
                continue
            return numbers
        except ValueError:
            print("  输入格式错误，请输入数字并用空格分隔")


def get_menu_choice() -> str:
    """获取菜单选项（1-6）"""
    # TODO: 返回 input 的结果，去掉首尾空格
    menuKey: list[str] = ["1", "2", "3", "4", "5", "6"]
    inputStr: str = input("请输入菜单选项（1-6）: ").strip()
    if inputStr in menuKey:
        return inputStr
    else:
        print("  输入错误，请输入1-6之间的数字")
        return get_menu_choice()


# ============================================================
# 历史记录
# ============================================================

history: list[dict] = []


def add_to_history(operation: str, numbers: list[float], result: float) -> None:
    """把一次运算记录到历史中"""
    # TODO: append 一个 dict，包含 operation、numbers、result
    history.append({"operation": operation, "numbers": numbers, "result": result})


def show_history() -> None:
    """显示所有历史记录"""
    if not history:
        print("\n  暂无历史记录\n")
        return
    print(f"\n===== 历史记录（共{len(history)}条）=====")
    # TODO: 遍历 history，格式化输出每条
    # 例: [1] 加法: 1 + 2 + 3 = 6
    for i, item in enumerate(history, 1):
        print(f"[{i}] {item['operation']}: {' '.join(map(str, item['numbers']))} = {item['result']:.2f}")


# ============================================================
# 核心运算流程
# ============================================================

def do_operation(choice: str) -> None:
    """根据菜单选项执行对应运算"""
    op_map = {
        "1": ("加法", calc.add),
        "2": ("减法", calc.subtract),
        "3": ("乘法", calc.multiply),
        "4": ("除法", calc.divide),
    }
    op_name, op_func = op_map[choice]

    numbers = get_numbers(f"输入要{op_name}的数字: ")

    try:
        # TODO: 调用 op_func(*numbers) 得到结果
        result = op_func(*numbers)
        # TODO: 打印结果（保留2位小数）
        print(f"  结果: {result:.2f}")
        # TODO: 记录到历史
        add_to_history(op_name, numbers, result)
    except ValueError as e:
        # TODO: 捕获除零等错误
        print(e)


# ============================================================
# 主程序
# ============================================================

def main() -> None:
    """主菜单循环"""
    print("=" * 40)
    print("         命令行计算器 v1.0")
    print("=" * 40)

    while True:
        print("\n请选择运算：")
        print("1. 加法    2. 减法    3. 乘法")
        print("4. 除法    5. 历史记录  6. 退出")
        choice = get_menu_choice()

        if choice in ("1", "2", "3", "4"):
            do_operation(choice)
        elif choice == "5":
            show_history()
        elif choice == "6":
            print("再见！")
            break
        else:
            print("  请输入 1-6")


if __name__ == "__main__":
    main()
