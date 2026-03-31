# 4-13 buffet
buffet_foods = ('pizza', 'pasta', 'salad', 'soup', 'bread')
for food in buffet_foods:
    print(f"{food.title()}")
# buffet_foods[0] = 'steak'  # 这行代码会报错，因为元组内的值不可修改
buffet_foods = ('steak', 'seafood', 'salad', 'soup', 'bread')
for food in buffet_foods:
    print(food)