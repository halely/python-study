import game_utils as gu

# ============================================================
# import game_utils 或 from game_utils import ...
# 写 main() 函数实现游戏循环
# 用 if __name__ == "__main__": 调用 main()
# ============================================================


def play_one_round(target: int) -> int:
    """玩一局猜数字游戏"""
    attempts: int = 0
    while True:
        guess: int = gu.get_valid_int("请输入你猜的数字（1-10）：", 1, 10)
        print(f"你猜的数字是 {guess}")
        attempts += 1
        print(gu.get_hint(guess, target))
        if guess == target:
            return attempts


def main() -> None:
    """主函数"""
    while True:
        target = gu.generate_target(1, 10)
        attempts = play_one_round(target)
        print(f"你用了{attempts}次猜对了目标数字{target}")
        again = input("是否继续游戏？（y/n）：")
        if again.lower() != "y":
            print("游戏结束，感谢参与！")
            break

if __name__ == "__main__":
    main()