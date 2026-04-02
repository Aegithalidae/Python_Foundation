# 6-1 person
familiar_person = {
    "first_name": "Mike",
    "last_name": "Smith",
    "age": 26,
    "city": "Shanghai",
}
for key in familiar_person:
    print(f"{key}: {familiar_person[key]}")

# 还可以使用 .items() 方法
for key, value in familiar_person.items():
    print(f"{key}: {value}")
