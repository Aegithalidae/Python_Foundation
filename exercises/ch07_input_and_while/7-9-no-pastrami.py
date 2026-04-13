# 7-9 No Pastrami
sandwich_orders = [
    "pastrami",
    "chicken",
    "pastrami",
    "beef",
    "pastrami",
    "veggie",
    "pastrami",
    "pastrami",
    "pastrami",
]
print("Sorry , we have sold out pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
