# 4-1 pizza
pizzas = ['pepperoni', 'mushroom', 'pineapple']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print(f'''{pizzas[0].title()} pizza is my favorite! 
I really love {pizzas[1].title()} pizza, too!
I can't stand {pizzas[2].title()} pizza.\n''')
# f-string不允许跨行，所以这里使用了三引号来创建多行字符串。