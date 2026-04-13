# 8-12 sandwich
def sandwich(*ingredients):
    print("\nHere are your sandwich ingredients")
    for _ in ingredients:
        print(f"- {_}")


# 第一次调用：经典组合
sandwich("培根", "生菜", "番茄")

# 第二次调用：简单的芝士党
sandwich("切达芝士", "火腿")

# 第三次调用：豪华全家桶
sandwich("牛肉", "酸黄瓜", "洋葱", "蛋黄酱", "牛油果", "煎蛋")
