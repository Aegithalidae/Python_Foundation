# 6-5 rivers
river_map = {
    "Nile": ["Egypt", "Sudan", "Ethiopia", "Uganda"],  # 列表存储多个国家
    "Amazon": ["Brazil", "Peru", "Colombia"],
    "Yangtze": ["China"],
}

for river, nations in river_map.items():
    print(f"The {river} runs through {nations} ")
    print(river)
    print(nations)
    print("\n")
