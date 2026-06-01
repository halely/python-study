def exercise_password(pws: str) -> bool:
    """
    密码验证
    - 密码长度必须大于等于6
    - 包�含字母和数字
    - 包含特殊字符
    """
    if len(pws) < 8:  # 密码长度必须大于等于8
        print(f"密码 {pws} 的长度必须大于等于8")
        return False
    if not any(char.isdigit() for char in pws):  # 密码必须包含数字
        print(f"密码 {pws} 必须包含数字")
        return False
    if not any(char.isalpha() for char in pws):  # 密码必须包含字母
        print(f"密码 {pws} 必须包含字母")
        return False
    if not any(char in "!@#$%^&*()-_+={[}]|;:'\",.<>?" for char in pws):  # 密码必须包含特殊字符
        print(f"密码 {pws} 必须包含特殊字符")
        return False
    if pws.lower() == pws or pws.upper() == pws:  # 密码必须包含大小写字母
        print(f"密码 {pws} 必须包含大小写字母")
        return False
    return True
    

exercise_password("12345aa$aa6")  