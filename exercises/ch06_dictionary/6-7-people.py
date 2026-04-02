# 6-7 people
familiar_person = {
    "son": {
        "first_name": "Mike",
        "last_name": "Smith",
        "age": 26,
        "city": "Shanghai",
        "gender": "male",
    },
    "daughter": {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 25,
        "city": "Shanghai",
        "gender": "female",
    },
    "father": {
        "first_name": "Leo",
        "last_name": "Smith",
        "age": 55,
        "city": "Shanghai",
        "gender": "male",
    },
    "Mather": {
        "first_name": "Silas",
        "last_name": "Smith",
        "age": 54,
        "city": "Shanghai",
        "gender": "female",
    },
}

for name, info in familiar_person.items():
    full_name = f"{info['first_name']} {info['last_name']}"

    print(f"{name}'s full name is {full_name}")
    if info["gender"] == "male":
        print(f"He is {info['age']} years old and lives in {info['city']}")
        print("\n")
    elif info["gender"] == "female":
        print(f"She is {info['age']} years old and lives in {info['city']}")
        print("\n")

# 6-8、6-9、6-10、6-11、6-12与本题完全一致，故不再记录
