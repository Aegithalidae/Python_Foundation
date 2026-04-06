# 7-8 Delicatessen
sandwich_orders = ["pastrami", "chicken", "pastrami", "beef", "pastrami", "veggie"]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwiches:
    print(sandwich)
