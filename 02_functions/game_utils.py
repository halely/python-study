import random


# ============================================================
# 公开函数（供外部导入使用）
# ============================================================
def generate_target(min_num: int, max_num: int) -> int:
    """生成一个随机数，范围为 min_num 到 max_num"""
    return random.randint(min_num, max_num)

def get_hint(guess: int, target: int) -> str:
    """根据猜的数字和目标数字，返回提示"""
    if guess == target:
        return "恭喜你猜对了！"
    elif guess < target:
        return "猜的数字太小了"
    else:
        return "猜的数字太大了"

def get_valid_int(prompt: str, min_val: int, max_val: int) -> int:
    """获取一个在指定范围内的整数输入"""
    while True:
        try:
            guess: int = int(input(prompt))
            if min_val <= guess <= max_val:
                return guess
            print(f"请输入一个在 {min_val} 到 {max_val} 之间的整数")
        except ValueError:
            print("请输入一个整数")
if __name__ == "__main__":
    print(generate_target(1, 10))
    print(get_hint(5, 7))