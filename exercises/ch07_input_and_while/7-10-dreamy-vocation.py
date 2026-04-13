# 7-10 Dreamy_vocation
Dreamy_vocation = {}
active = True

while active:
    name = input("Please enter your name.")
    vocation = input(
        "If you could visit some places in the world, where would you go?(split by ',')"
    )
    vocation_list = [vocation.strip() for vocation in vocation.split(",")]

    if name not in Dreamy_vocation:
        Dreamy_vocation[name] = []
    Dreamy_vocation[name].extend(vocation_list)

    check = input("Any where to add?(yes/no)")
    if check == "no":
        active = False

print("\n--- Investigate Result ---")
for name, vocations in Dreamy_vocation.items():
    print(f"{name} would like to go to:")
    for place in vocations:
        print(f"  - {place}")
