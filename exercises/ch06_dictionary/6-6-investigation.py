# 6-6 调查：处理不规范的字典键名与名单匹配

# 原始调查数据：模拟现实中大小写不规范的录入情况
favorite_languages = {
    "Jen": "python",
    "saRaH": "c",
    "edward": "ruby",
    "phil": "python",
}

# 数据标准化（Normalization）：
# 使用字典推导式创建一个键全部为小写的新字典。
# 这样做是为了在后续查询中实现 O(1) 的常数级查找效率，同时解决大小写匹配问题。
normalize_dict = {k.lower(): v for k, v in favorite_languages.items()}

# 待检查的参与者名单（包含不同的大小写格式）
operator_name = ["jEn", "mIke", "sarah", "john"]

for name in operator_name:
    # 统一转为小写，以便与标准化后的字典键进行比对
    clean_name = name.lower()

    # 利用字典（哈希表）的高性能查找确认该人是否已完成调查
    if clean_name in normalize_dict:
        # title() 让输出的名字格式更统一美观（首字母大写）
        print(f"Thank you {clean_name.title()}, we appreciate your contribution")
    else:
        print(f"Please accept the investigation, {clean_name.title()}")
