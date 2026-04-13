# 7-4 pizza toppings
toppings = "\nPlease choose your toppings:"
toppings += "\nEnter 'quit' to end"
toppings_menu = []

active = True
while active:
    topping = input(toppings)
    if topping == "quit":
        active = False
        # 在下一轮循环开始时退出，换成break更直接
    else:
        toppings_menu.append(topping)
        print(f"""You have chosen {topping}. And here are your menu: {toppings_menu}""")
