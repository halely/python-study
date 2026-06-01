def shopping_list_fn() -> None:
    """
    场景：购物清单管理
    - 用 list 存储购物清单
    - 用 dict 存储商品价格
    - 用 set 去重
    - 用 tuple 存储不可变的分类信息
    """
    print("=" * 40)
    print("购物清单管理")
    print("=" * 40)

    # list: 购物清单
    shopping_list: list[str] = ["牛奶", "面包", "鸡蛋", "牛奶", "水果"]
    print(f"原始购物清单: {shopping_list}")

    # set: 去重后的购物清单
    unique_items: set[str] = set(shopping_list)
    print(f"去重后的购物清单: {unique_items}")

    # dict: 商品价格
    prices: dict[str, float] = {
        "牛奶": 3.5,
        "面包": 2.0,
        "鸡蛋": 0.5,
        "水果": 5.0
    }
    print(f"商品价格: {prices}")

    # tuple: 分类信息（固定不变）
    categories: tuple[str, ...] = ("乳制品", "面包", "蛋类", "水果")
    print(f"商品分类: {categories}")

shopping_list_fn()