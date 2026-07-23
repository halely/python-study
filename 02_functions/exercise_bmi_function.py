def calculate_bmi(weight: float, height: float) -> float:
    """根据体重(kg)和身高(m)计算 BMI 指数"""
    if height <= 0 or weight <= 0:
        raise ValueError("身高和体重必须大于0")
    bmi: float = weight / (height ** 2)
    return bmi


def get_bmi_status(bmi: float) -> str:
    """根据 BMI 值返回体重状态"""
    if bmi < 18.5:
        return "体重过轻"
    elif bmi < 24:
        return "体重正常"
    elif bmi < 27:
        return "体重过重"
    else:
        return "体重肥胖"


def main() -> None:
    """主函数"""
    weight: float = float(input("请输入体重（单位：千克）："))
    height: float = float(input("请输入身高（单位：米）："))
    bmi: float = calculate_bmi(weight, height)
    status: str = get_bmi_status(bmi)
    print(f"BMI值为：{bmi:.2f}")
    print(f"体重状态：{status}")


if __name__ == "__main__":
    main()