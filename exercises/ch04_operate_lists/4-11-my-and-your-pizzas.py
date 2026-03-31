# 4-11 my pizza and your pizza
my_pizzas = ['pepperoni', 'mushroom', 'pineapple']
my_pizzas.append('extra cheese')
friend_pizzas = my_pizzas[:]
print("My favorite pizzas are:")
print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)
friend_pizzas.append('bbq chicken')
print("\nMy favorite pizzas are:")
print(my_pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)
for pizza in friend_pizzas:
    print(pizza)