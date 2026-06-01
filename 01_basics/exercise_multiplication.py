def multiplication_table() -> None:
    """
    乘法口诀表
    - 用 for 循环生成乘法表
    """
    for x in range(1, 10):
        for y in range(1, 10):
            print(f"{x} x {y} = {x * y}", end="\t")  # end="\t" 用制表符分隔每列
        print()  # 每行结束后换行
multiplication_table()