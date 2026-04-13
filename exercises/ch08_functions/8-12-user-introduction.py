# 8-13 user_introduction
def build_profile(first, last, **user_info):
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "wu",
    "kaiyuan",
    location="Shiyan",
    field="Ensemble forecast",
    exercise="street workout",
    tall=178,
)
print("profile = ", user_profile)
